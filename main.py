from curriculoLattes import CurriculoLattes
from processadorXmlLattes import ProcessadorXmlLattes
import pprint

caminho_xml = "xmls/curriculo.xml"
curriculoLattes = ProcessadorXmlLattes(caminho_xml)

dados_gerais = curriculoLattes.busca_dados_gerais()
formacao_academica = curriculoLattes.busca_formacao_academica()
atuacoes_profissionais = curriculoLattes.busca_atuações_profissionais()

pprint.pprint({
    "dados": dados_gerais,
    "formacao": formacao_academica,
    "atuacoes": atuacoes_profissionais
})