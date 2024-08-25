from lxml import etree

class ProcessadorXmlLattes:
    def __init__(self, caminho_xml: str) -> None:
        self.caminho_xml = caminho_xml
        try:
            self.root_xml = etree.parse(caminho_xml).getroot()
        except (etree.XMLSyntaxError, OSError) as e:
            raise ValueError(f"Erro ao processar o arquivo XML: {e}")

    def _normaliza_texto(self, texto: str) -> str:
        """Normaliza o texto removendo espaços desnecessários e capitalizando a primeira letra."""
        return texto.strip().capitalize() if texto else "Não encontrado"

    def _formata_data(self, mes: str, ano: str) -> str:
        """Formata a data como MM/AAAA."""
        if mes.isdigit() and ano.isdigit():
            return f"{mes.zfill(2)}/{ano}"
        return "Data inválida"

    def busca_dados_gerais(self) -> dict:
        try:
            dados_gerais = self.root_xml.find(".//DADOS-GERAIS")
            resumo_cv = self.root_xml.find(".//RESUMO-CV")
            return {
                "nome_completo": self._normaliza_texto(dados_gerais.get("NOME-COMPLETO", "Não encontrado")),
                "nacionalidade": self._normaliza_texto(dados_gerais.get("PAIS-DE-NACIONALIDADE", "Não encontrado")),
                "resumo_cv": self._normaliza_texto(resumo_cv.get("TEXTO-RESUMO-CV-RH", "Resumo não encontrado")) if resumo_cv is not None else "Resumo não encontrado"
            }
        except Exception as e:
            raise ValueError(f"Erro ao buscar dados gerais: {e}")

    def busca_formacao_academica(self) -> list:
        try:
            formacoes = []
            for formacao in self.root_xml.findall(".//FORMACAO-ACADEMICA-TITULACAO/*"):
                formacoes.append({
                    "nome_curso": self._normaliza_texto(formacao.get("NOME-CURSO", "Não encontrado")),
                    "nome_instituicao": self._normaliza_texto(formacao.get("NOME-INSTITUICAO", "Não encontrado")),
                    "ano_conclusao": formacao.get("ANO-DE-CONCLUSAO", "Não encontrado")
                })
            return formacoes
        except Exception as e:
            raise ValueError(f"Erro ao buscar formação acadêmica: {e}")

    def busca_atuacoes_profissionais(self) -> list:
        try:
            atuacoes = []
            for atuacao in self.root_xml.findall(".//ATUACAO-PROFISSIONAL"):
                vinculo = atuacao.find(".//VINCULOS")
                atuacoes.append({
                    "nome_instituicao": self._normaliza_texto(atuacao.get("NOME-INSTITUICAO", "Não encontrado")),
                    "cargo_ocupado": self._normaliza_texto(vinculo.get("OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO", "Não encontrado")) if vinculo is not None else "Não encontrado",
                    "data_inicio": self._formata_data(vinculo.get('MES-INICIO', ''), vinculo.get('ANO-INICIO', '')) if vinculo is not None else "Não encontrado",
                    "data_termino": self._formata_data(vinculo.get('MES-FIM', ''), vinculo.get('ANO-FIM', '')) if vinculo is not None else "Não encontrado"
                })
            return atuacoes
        except Exception as e:
            raise ValueError(f"Erro ao buscar atuações profissionais: {e}")

    def busca_atividades_ensino(self) -> list:
        try:
            disciplinas = []
            for ensino in self.root_xml.findall(".//ENSINO"):
                for disciplina in ensino.findall(".//DISCIPLINA"):
                    if disciplina.text:
                        disciplinas.append(self._normaliza_texto(disciplina.text))
            return disciplinas
        except Exception as e:
            raise ValueError(f"Erro ao buscar atividades de ensino: {e}")

    def busca_atividades_pesquisa(self) -> list:
        try:
            linhas_pesquisa = []
            for linha in self.root_xml.findall(".//LINHA-DE-PESQUISA"):
                linhas_pesquisa.append({
                    "titulo": self._normaliza_texto(linha.get("TITULO-DA-LINHA-DE-PESQUISA", "Não encontrado")),
                    "descricao": self._normaliza_texto(linha.get("OBJETIVOS-LINHA-DE-PESQUISA", "Não encontrado"))
                })
            return linhas_pesquisa
        except Exception as e:
            raise ValueError(f"Erro ao buscar atividades de pesquisa: {e}")

    def busca_participacao_projetos(self) -> list:
        try:
            projetos = []
            for projeto in self.root_xml.findall(".//PARTICIPACAO-EM-PROJETO"):
                projeto_info = projeto.find(".//PROJETO-DE-PESQUISA")
                if projeto_info is not None:
                    projetos.append({
                        "nome_projeto": self._normaliza_texto(projeto_info.get("NOME-DO-PROJETO", "Não encontrado")),
                        "situacao_projeto": self._normaliza_texto(projeto_info.get("SITUACAO", "Não encontrado")),
                        "descricao_projeto": self._normaliza_texto(projeto_info.get("DESCRICAO-DO-PROJETO", "Não encontrado"))
                    })
            return projetos
        except Exception as e:
            raise ValueError(f"Erro ao buscar participação em projetos: {e}")

    def busca_palavras_chave(self) -> list:
        try:
            palavras_chave = []
            for palavra in self.root_xml.findall(".//PALAVRAS-CHAVE//PALAVRA-CHAVE"):
                if palavra.text:
                    palavras_chave.append(self._normaliza_texto(palavra.get("PALAVRA-CHAVE-1", "Não encontrado")))
            return palavras_chave
        except Exception as e:
            raise ValueError(f"Erro ao buscar palavras-chave: {e}")

    def busca_areas_conhecimento(self) -> list:
        try:
            areas_conhecimento = []
            for area in self.root_xml.findall(".//AREA-DO-CONHECIMENTO"):
                areas_conhecimento.append({
                    "grande_area": self._normaliza_texto(area.get("NOME-GRANDE-AREA-DO-CONHECIMENTO", "Não encontrado")),
                    "area": self._normaliza_texto(area.get("NOME-DA-AREA-DO-CONHECIMENTO", "Não encontrado")),
                    "sub_area": self._normaliza_texto(area.get("NOME-DA-SUB-AREA-DO-CONHECIMENTO", "Não encontrado"))
                })
            return areas_conhecimento
        except Exception as e:
            raise ValueError(f"Erro ao buscar áreas do conhecimento: {e}")
