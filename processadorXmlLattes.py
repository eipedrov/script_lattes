from lxml import etree

class ProcessadorXmlLattes:
    def __init__(self, caminho_xml: str) -> None:
        self.caminho_xml = caminho_xml
        try:
            self.root_xml = etree.parse(caminho_xml).getroot()
        except (etree.XMLSyntaxError, OSError) as e:
            raise ValueError(f"Erro ao processar o arquivo XML: {e}")

    def busca_dados_gerais(self) -> dict:
        try:
            dados_gerais = self.root_xml.find(".//DADOS-GERAIS")
            resumo_cv = self.root_xml.find(".//RESUMO-CV")
            return {
                "nome_completo": dados_gerais.get("NOME-COMPLETO", "Não encontrado"),
                "nacionalidade": dados_gerais.get("PAIS-DE-NACIONALIDADE", "Não encontrado"),
                "resumo_cv": resumo_cv.get("TEXTO-RESUMO-CV-RH", "Resumo não encontrado") if resumo_cv is not None else "Resumo não encontrado"
            }
        except Exception as e:
            raise ValueError(f"Erro ao buscar dados gerais: {e}")

    def busca_formacao_academica(self) -> list:
        try:
            formacoes = []
            for formacao in self.root_xml.findall(".//FORMACAO-ACADEMICA-TITULACAO/*"):
                formacoes.append({
                    "nome_curso": formacao.get("NOME-CURSO", "Não encontrado"),
                    "nome_instituicao": formacao.get("NOME-INSTITUICAO", "Não encontrado"),
                    "ano_conclusao": formacao.get("ANO-DE-CONCLUSAO", "Não encontrado")
                })
            return formacoes
        except Exception as e:
            raise ValueError(f"Erro ao buscar formação acadêmica: {e}")

    def busca_atuações_profissionais(self) -> list:
        try:
            atuacoes = []
            for atuacao in self.root_xml.findall(".//ATUACAO-PROFISSIONAL"):
                vinculo = atuacao.find(".//VINCULOS")
                atuacoes.append({
                    "nome_instituicao": atuacao.get("NOME-INSTITUICAO", "Não encontrado"),
                    "cargo_ocupado": vinculo.get("OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO", "Não encontrado") if vinculo is not None else "Não encontrado",
                    "data_inicio": f"{vinculo.get('MES-INICIO', 'Não encontrado')}/{vinculo.get('ANO-INICIO', 'Não encontrado')}" if vinculo is not None else "Não encontrado",
                    "data_termino": f"{vinculo.get('MES-FIM', 'Não encontrado')}/{vinculo.get('ANO-FIM', 'Não encontrado')}" if vinculo is not None else "Não encontrado"
                })
            return atuacoes
        except Exception as e:
            raise ValueError(f"Erro ao buscar atuações profissionais: {e}")

    def busca_atividades_ensino(self) -> list:
        try:
            disciplinas = []
            for ensino in self.root_xml.findall(".//ENSINO"):
                for disciplina in ensino.findall(".//DISCIPLINA"):
                    disciplinas.append(disciplina.text)
            return disciplinas
        except Exception as e:
            raise ValueError(f"Erro ao buscar atividades de ensino: {e}")

    def busca_atividades_pesquisa(self) -> list:
        try:
            linhas_pesquisa = []
            for linha in self.root_xml.findall(".//LINHA-DE-PESQUISA"):
                linhas_pesquisa.append({
                    "titulo": linha.get("TITULO-DA-LINHA-DE-PESQUISA", "Não encontrado"),
                    "descricao": linha.get("OBJETIVOS-LINHA-DE-PESQUISA", "Não encontrado")
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
                        "nome_projeto": projeto_info.get("NOME-DO-PROJETO", "Não encontrado"),
                        "situacao_projeto": projeto_info.get("SITUACAO", "Não encontrado"),
                        "descricao_projeto": projeto_info.get("DESCRICAO-DO-PROJETO", "Não encontrado")
                    })
            return projetos
        except Exception as e:
            raise ValueError(f"Erro ao buscar participação em projetos: {e}")

    def busca_palavras_chave(self) -> list:
        try:
            palavras_chave = []
            for palavra in self.root_xml.findall(".//PALAVRAS-CHAVE//PALAVRA-CHAVE"):
                palavras_chave.append(palavra.get("PALAVRA-CHAVE-1", "Não encontrado"))
            return palavras_chave
        except Exception as e:
            raise ValueError(f"Erro ao buscar palavras-chave: {e}")

    def busca_areas_conhecimento(self) -> list:
        try:
            areas_conhecimento = []
            for area in self.root_xml.findall(".//AREA-DO-CONHECIMENTO"):
                areas_conhecimento.append({
                    "grande_area": area.get("NOME-GRANDE-AREA-DO-CONHECIMENTO", "Não encontrado"),
                    "area": area.get("NOME-DA-AREA-DO-CONHECIMENTO", "Não encontrado"),
                    "sub_area": area.get("NOME-DA-SUB-AREA-DO-CONHECIMENTO", "Não encontrado")
                })
            return areas_conhecimento
        except Exception as e:
            raise ValueError(f"Erro ao buscar áreas do conhecimento: {e}")