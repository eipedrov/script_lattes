import os
import pandas as pd
import json
from processadorXmlLattes import ProcessadorXmlLattes  # Importa a classe que processa os arquivos XML

def atualizar_planilha_dados_gerais(dados_novos, caminho_saida):
    """Função para atualizar a planilha 'Dados Gerais' com dados quantitativos dos pesquisadores.
    Se o pesquisador já existir na planilha, os valores serão atualizados."""
    caminho_planilha = os.path.join(caminho_saida, 'Dados_gerais.xlsx')

    # Se o arquivo já existir, carrega a planilha existente
    if os.path.exists(caminho_planilha):
        df_existente = pd.read_excel(caminho_planilha)
        
        # Verifica se o pesquisador já está na planilha
        if dados_novos["Nome"] in df_existente["Nome"].values:
            # Atualiza os valores do pesquisador
            df_existente.loc[df_existente["Nome"] == dados_novos["Nome"], "Artigos Publicados"] = dados_novos["Artigos Publicados"]
            df_existente.loc[df_existente["Nome"] == dados_novos["Nome"], "Trabalhos em Eventos"] = dados_novos["Trabalhos em Eventos"]
        else:
            # Adiciona um novo pesquisador
            df_novo = pd.DataFrame([dados_novos])
            df_existente = pd.concat([df_existente, df_novo], ignore_index=True)

        df_existente.to_excel(caminho_planilha, index=False)
    else:
        # Se o arquivo não existir, cria uma nova planilha com o primeiro pesquisador
        df_novo = pd.DataFrame([dados_novos])
        df_novo.to_excel(caminho_planilha, index=False)

    print(f"Planilha 'Dados Gerais' atualizada em: {caminho_planilha}")

def salvar_dados_detalhados(dados_detalhados, caminho_saida, formato_saida):
    """Função para salvar os dados detalhados de um pesquisador em JSON ou Excel com 3 abas no Excel"""
    nome_arquivo = os.path.join(caminho_saida, dados_detalhados["Nome"].replace(" ", "_") + "_detalhado")

    if formato_saida == 'json':
        with open(nome_arquivo + '.json', 'w', encoding='utf-8') as f:
            json.dump(dados_detalhados, f, ensure_ascii=False, indent=4)
        print(f"Dados detalhados salvos em: {nome_arquivo}.json")

    elif formato_saida == 'excel':
        # Aba 1: Dados Gerais
        df_dados_gerais = pd.DataFrame([{
            "Nome": dados_detalhados["Nome"],
            "Nacionalidade": dados_detalhados["Nacionalidade"],
            "Resumo do CV": dados_detalhados["Resumo do CV"]
        }])

        # Aba 2: Artigos Publicados
        df_artigos = pd.DataFrame(dados_detalhados["Artigos Publicados"])

        # Aba 3: Trabalhos em Eventos
        df_trabalhos_eventos = pd.DataFrame(dados_detalhados["Trabalhos em Eventos"])

        # Escrevendo os dados em diferentes abas da planilha
        with pd.ExcelWriter(nome_arquivo + '.xlsx', engine='openpyxl') as writer:
            df_dados_gerais.to_excel(writer, sheet_name='Dados Gerais', index=False)
            df_artigos.to_excel(writer, sheet_name='Artigos Publicados', index=False)
            df_trabalhos_eventos.to_excel(writer, sheet_name='Trabalhos em Eventos', index=False)

        print(f"Dados detalhados salvos em: {nome_arquivo}.xlsx")

def processar_arquivo_xml(caminho_xml, formato_saida, caminho_saida, tipo_saida):
    """Função para processar um único arquivo XML e gerar os dados detalhados ou resumidos."""
    try:
        # Instancia a classe para processar o XML
        processador = ProcessadorXmlLattes(caminho_xml)
        
        # Extrai os dados do pesquisador
        dados_gerais = processador.busca_dados_gerais()
        artigos_publicados = processador.busca_artigos_publicados()
        trabalhos_em_eventos = processador.busca_trabalhos_em_eventos()
        
        # Organiza os dados detalhados
        dados_detalhados = {
            "Nome": dados_gerais["nome_completo"],
            "Nacionalidade": dados_gerais["nacionalidade"],
            "Resumo do CV": dados_gerais["resumo_cv"],
            "Artigos Publicados": artigos_publicados,
            "Trabalhos em Eventos": trabalhos_em_eventos
        }

        # Organiza os dados numéricos (quantidade de produções)
        dados_numericos = {
            "Nome": dados_gerais["nome_completo"],
            "Artigos Publicados": len(artigos_publicados),
            "Trabalhos em Eventos": len(trabalhos_em_eventos)
        }

        # Atualiza a planilha "Dados Gerais"
        atualizar_planilha_dados_gerais(dados_numericos, caminho_saida)

        # Gera os dados detalhados se necessário
        if tipo_saida == 'detalhado':
            salvar_dados_detalhados(dados_detalhados, caminho_saida, formato_saida)

        print("Dados gerais e detalhados processados com sucesso!")
        
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)
