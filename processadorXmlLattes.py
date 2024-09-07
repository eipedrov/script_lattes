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

    # Função corrigida para buscar dados gerais
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

    # Função corrigida para buscar atuações profissionais
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

    # Outras funções de busca de produções e dados
    def busca_artigos_publicados(self) -> list:
        try:
            artigos = []
            for artigo in self.root_xml.findall(".//ARTIGO-PUBLICADO"):
                dados = artigo.find(".//DADOS-BASICOS-DO-ARTIGO")
                titulo = dados.attrib.get('TITULO-DO-ARTIGO', 'Sem título')
                ano = dados.attrib.get('ANO-DO-ARTIGO', 'Sem ano')
                autores = [self._normaliza_texto(autor.attrib.get('NOME-COMPLETO-DO-AUTOR')) for autor in artigo.findall(".//AUTORES")]
                artigos.append({
                    "titulo": titulo,
                    "ano": ano,
                    "autores": autores
                })
            return artigos
        except Exception as e:
            raise ValueError(f"Erro ao buscar artigos publicados: {e}")

    def busca_trabalhos_em_eventos(self) -> list:
        try:
            trabalhos = []
            for trabalho in self.root_xml.findall(".//TRABALHO-EM-EVENTOS"):
                dados = trabalho.find(".//DADOS-BASICOS-DO-TRABALHO")
                titulo = dados.attrib.get('TITULO-DO-TRABALHO', 'Sem título')
                ano = dados.attrib.get('ANO-DO-TRABALHO', 'Sem ano')
                autores = [self._normaliza_texto(autor.attrib.get('NOME-COMPLETO-DO-AUTOR')) for autor in trabalho.findall(".//AUTORES")]
                trabalhos.append({
                    "titulo": titulo,
                    "ano": ano,
                    "autores": autores
                })
            return trabalhos
        except Exception as e:
            raise ValueError(f"Erro ao buscar trabalhos em eventos: {e}")

    # Outras funções como busca_formacao_academica, busca_participacao_projetos etc.

    def busca_todas_as_producoes(self) -> dict:
        """Busca todas as produções acadêmicas (artigos, trabalhos em eventos, etc.)"""
        return {
            "dados_gerais": self.busca_dados_gerais(),
            "artigos_publicados": self.busca_artigos_publicados(),
            "trabalhos_em_eventos": self.busca_trabalhos_em_eventos(),
            "atuacoes_profissionais": self.busca_atuacoes_profissionais()
        }
