from curriculoLattes import CurriculoLattes
from processador_xml_lattes import ProcessadorXmlLattes
from salvador_dados_lattes import salvadorDadosLattes

def main(caminho_xml, formato_saida, caminho_saida):
    try:
        processador = ProcessadorXmlLattes(caminho_xml)
        
        dados_gerais = processador.busca_dados_gerais()
        formacao_academica = processador.busca_formacao_academica()
        atuacoes_profissionais = processador.busca_atuacoes_profissionais()
        atividades_ensino = processador.busca_atividades_ensino()
        atividades_pesquisa = processador.busca_atividades_pesquisa()
        participacao_projetos = processador.busca_participacao_projetos()
        palavras_chave = processador.busca_palavras_chave()
        areas_conhecimento = processador.busca_areas_conhecimento()

        dados = {
            "Dados Gerais": dados_gerais,
            "Formação Acadêmica": formacao_academica,
            "Atuações Profissionais": atuacoes_profissionais,
            "Atividades de Ensino": atividades_ensino,
            "Atividades de Pesquisa": atividades_pesquisa,
            "Participação em Projetos": participacao_projetos,
            "Palavras-Chave": palavras_chave,
            "Áreas do Conhecimento": areas_conhecimento,
        }

        salvador = SalvadorDadosLattes(dados)

        if formato_saida == 'json':
            salvador.salvar_como_json(caminho_saida)
        elif formato_saida == 'csv':
            salvador.salvar_como_csv(caminho_saida)
        elif formato_saida == 'excel':
            salvador.salvar_como_excel(caminho_saida)
        else:
            print("Formato de saída inválido. Escolha entre 'json', 'csv' ou 'excel'.")

    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python main.py <caminho_arquivo_xml> <formato_saida> <caminho_saida>")
        sys.exit(1)

    caminho_xml = sys.argv[1]
    formato_saida = sys.argv[2]
    caminho_saida = sys.argv[3]
    main(caminho_xml, formato_saida, caminho_saida)
