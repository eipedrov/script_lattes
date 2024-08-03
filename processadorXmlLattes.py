from lxml import etree

class ProcessadorXmlLattes():
    caminho_xml = None
    root_xml = None

    def __init__(self, caminho_xml) -> None:
        self.caminho_xml = caminho_xml
        self.root_xml = etree.parse(caminho_xml).getroot()
    

    def buscaResumo(self) -> str:
        elemento = self.root_xml.find(".//RESUMO-CV")
        if elemento is not None:
            resumo_curriculo = elemento.get("TEXTO-RESUMO-CV-RH")
            if resumo_curriculo is not None:
                return resumo_curriculo
            else:
                print("Resumo do curriculo não encontrado!")
                return None
        else:
            print("Tag com o atributo especificado não encontrada")
            return None
