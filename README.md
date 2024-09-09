
# Projeto: Processamento de Currículos Lattes com Extração de Dados e Geração de Planilhas

Este projeto tem como objetivo processar currículos Lattes em formato XML, extraindo dados detalhados e numéricos sobre a produção acadêmica de pesquisadores. Os dados extraídos podem ser salvos em formatos **JSON** ou **Excel**, e há a opção de gerar tanto um arquivo detalhado quanto um resumo numérico das produções, que pode ser atualizado em uma planilha geral.

## Funcionalidades
- Processa arquivos XML de currículos Lattes.
- Extrai dados como:
  - Dados gerais do pesquisador.
  - Artigos publicados.
  - Trabalhos em eventos.
- Gera arquivos detalhados com os dados extraídos em **JSON** ou **Excel**.
- Gera um resumo numérico das produções acadêmicas do pesquisador.
- Suporte para processar múltiplos arquivos XML de uma pasta automaticamente.
- Atualiza uma planilha geral com o resumo numérico das produções.

## Tecnologias Utilizadas

### Linguagem de Programação:
- **Python 3.x**

### Bibliotecas:
- **lxml**: Para processar e extrair dados de arquivos XML.
- **pandas**: Para manipulação de dados e geração de arquivos Excel.
- **json**: Para manipulação de arquivos JSON.
- **os**: Para manipulação de arquivos e diretórios.
- **sys**: Para tratar argumentos de linha de comando.

## Requisitos de Sistema

- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python) instalado.

## Configuração do Ambiente

### 1. Clone o Repositório
```bash
git clone <url_do_repositorio>
cd <diretorio_do_projeto>
```

### 2. Crie um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:
```bash
python -m venv venv
```

Ative o ambiente virtual:
- No Windows:
    ```bash
    venv\Scripts\activate
    ```
- No Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

### 3. Instale as Dependências

No terminal, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

Verifique se as bibliotecas foram instaladas corretamente:
```bash
pip list
```

### 4. Estrutura do Projeto
- **main.py**: Script principal que processa os arquivos XML e gera as saídas.
- **processadorXmlLattes.py**: Contém a classe `ProcessadorXmlLattes`, responsável por processar e extrair dados dos currículos XML.
- **salvadorDadosLattes.py**: Contém a classe `SalvadorDadosLattes`, responsável por salvar os dados extraídos nos formatos **JSON** e **Excel**.

## Como Rodar o Projeto

### Rodando com um Único XML
Para processar um único arquivo XML e gerar a saída:
```bash
python main.py <caminho_da_pasta_xml> <formato_saida> <caminho_saida> <tipo_saida>
```

- `<caminho_da_pasta_xml>`: O caminho da pasta onde estão localizados os arquivos XML.
- `<formato_saida>`: O formato da saída. Pode ser **json** ou **excel**.
- `<caminho_saida>`: O caminho da pasta onde os arquivos de saída serão salvos.
- `<tipo_saida>`: Define o tipo de saída que será gerado:
  - `detalhado`: Gera uma planilha com todos os dados detalhados do pesquisador.
  - `resumo`: Gera uma planilha apenas com o resumo numérico das produções do pesquisador.
  - `ambos`: Gera tanto o arquivo detalhado quanto o resumo numérico.

### Exemplo:
```bash
python main.py ./xmls excel ./resultados ambos
```

Esse comando processará todos os arquivos XML na pasta `./xmls`, gerará saídas no formato Excel na pasta `./resultados`, e criará tanto o arquivo detalhado quanto o resumo numérico.

### Rodando para Múltiplos XMLs
Se você deseja processar todos os arquivos XML dentro de uma pasta, o script também oferece suporte para isso. Basta especificar a pasta onde os XMLs estão localizados e o script irá processar cada arquivo individualmente.

### Planilha Resumo
Caso o modo **resumo** ou **ambos** seja utilizado, o script atualizará uma planilha Excel com o resumo numérico das produções de cada pesquisador.

## Estrutura de Saída

### Arquivo Detalhado:
Este arquivo contém informações detalhadas do pesquisador, tais como:
- Dados gerais
- Artigos publicados
- Trabalhos em eventos

### Arquivo de Resumo:
Este arquivo contém um resumo numérico das produções, como:
- Número de artigos publicados
- Número de trabalhos apresentados em eventos

---

## Problemas Comuns

- **Problema**: O arquivo Excel gerado não contém dados.
  - **Solução**: Certifique-se de que os arquivos XML são válidos e estão no formato correto.

- **Problema**: O script não encontra o módulo `pandas` ou `lxml`.
  - **Solução**: Verifique se você instalou as dependências corretamente.


