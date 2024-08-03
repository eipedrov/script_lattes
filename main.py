from curriculoLattes import CurriculoLattes
from processadorXmlLattes import ProcessadorXmlLattes

caminho_xml = "xmls/curriculo.xml"
curriculoLattes = ProcessadorXmlLattes(caminho_xml)

resumo_cv = curriculoLattes.buscaResumo()
print(resumo_cv)