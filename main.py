import sys
import os
import pandas as pd
from processadorXmlLattes import ProcessadorXmlLattes
from salvadorDadosLattes import SalvadorDadosLattes

def processar_arquivo_xml(caminho_xml, formato_saida, caminho_saida, tipo_saida):
    """Função para processar um único arquivo XML e salvar as saídas."""
    try:
        # Instancia a classe para processar o XML
        processador = ProcessadorXmlLattes(caminho_xml)
        
        # Extrai os dados do pesquisador
        dados_gerais = processador.busca_dados_gerais()
        artigos_publicados = processador.busca_artigos_publicados()
        trabalhos_em_eventos = processador.busca_trabalhos_em_eventos()
        
        # Organiza os dados detalhados
        dados_detalhados = {
            "Dados Gerais": dados_gerais,
            "Artigos Publicados": artigos_publicados,
            "Trabalhos em Eventos": trabalhos_em_eventos
        }

        # Organiza os dados numéricos (quantidade de produções)
        dados_numericos = {
            "Nome": dados_gerais["nome_completo"],
            "Artigos Publicados": len(artigos_publicados),
            "Trabalhos em Eventos": len(trabalhos_em_eventos)
        }

        # Instancia a classe para salvar os dados
        salvador = SalvadorDadosLattes(dados_detalhados)

        # Verifica o tipo de saída e formato selecionados
        if tipo_saida == 'detalhado':
            if formato_saida == 'json':
                salvador.salvar_como_json(caminho_saida)
            elif formato_saida == 'excel':
                salvador.salvar_como_excel(caminho_saida)
            else:
                print("Formato de saída inválido. Escolha entre 'json' ou 'excel'.")
        elif tipo_saida == 'resumo':
            salvar_resumo_producao(caminho_saida, dados_numericos)
        elif tipo_saida == 'ambos':
            # Salva os dados detalhados
            if formato_saida == 'json':
                salvador.salvar_como_json(caminho_saida)
            elif formato_saida == 'excel':
                salvador.salvar_como_excel(caminho_saida)
            
            # Salva o resumo numérico
            salvar_resumo_producao(caminho_saida, dados_numericos)
        else:
            print("Tipo de saída inválido. Escolha entre 'detalhado', 'resumo' ou 'ambos'.")

    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

def processar_pasta(caminho_pasta, formato_saida, caminho_saida, tipo_saida):
    """Função para processar todos os arquivos XML em uma pasta."""
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".xml"):
            caminho_xml = os.path.join(caminho_pasta, arquivo)
            nome_arquivo = os.path.splitext(arquivo)[0]
            print(f"Processando arquivo: {caminho_xml}")
            caminho_saida_atual = os.path.join(caminho_saida, nome_arquivo)
            processar_arquivo_xml(caminho_xml, formato_saida, caminho_saida_atual, tipo_saida)

def salvar_resumo_producao(caminho_saida, dados_numericos):
    """Função para salvar ou atualizar uma planilha com o resumo numérico das produções"""
    caminho_planilha = caminho_saida + '_resumo.xlsx'
    nova_linha = pd.DataFrame([dados_numericos])
    
    if os.path.exists(caminho_planilha):
        # Se a planilha já existe, atualiza ela
        df_existente = pd.read_excel(caminho_planilha)
        df_atualizado = pd.concat([df_existente, nova_linha], ignore_index=True)
        df_atualizado.to_excel(caminho_planilha, index=False)
    else:
        # Se a planilha não existe, cria ela
        nova_linha.to_excel(caminho_planilha, index=False)

    print(f"Resumo numérico salvo/atualizado em {caminho_planilha}")

if __name__ == "__main__":
    # Verifica se os argumentos necessários foram passados
    if len(sys.argv) != 5:
        print("Uso: python main.py <caminho_da_pasta> <formato_saida> <caminho_saida> <tipo_saida>")
        sys.exit(1)

    caminho_pasta = sys.argv[1]
    formato_saida = sys.argv[2]
    caminho_saida = sys.argv[3]
    tipo_saida = sys.argv[4]

    # Chama a função para processar todos os arquivos XML da pasta
    processar_pasta(caminho_pasta, formato_saida, caminho_saida, tipo_saida)
