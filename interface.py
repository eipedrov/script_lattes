import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from main import processar_arquivo_xml  # Função que processa os arquivos XML

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo XML", filetypes=[("Arquivos XML", "*.xml")])
    if caminho_arquivo:
        entrada_arquivo.set(caminho_arquivo)

def selecionar_pasta_destino():
    pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")
    if pasta_destino:
        saida_pasta.set(pasta_destino)

def executar_processamento():
    arquivo_xml = entrada_arquivo.get()
    pasta_saida = saida_pasta.get()
    formato_saida = formato_var.get()
    tipo_saida = tipo_saida_var.get()

    if not arquivo_xml or not pasta_saida:
        messagebox.showwarning("Campos obrigatórios", "Por favor, selecione o arquivo XML e a pasta de destino.")
        return

    try:
        # Processa o arquivo e atualiza a planilha 'Dados Gerais' e os dados detalhados
        processar_arquivo_xml(arquivo_xml, formato_saida, pasta_saida, tipo_saida)

        messagebox.showinfo("Sucesso", "Arquivo processado com sucesso e dados detalhados/gerais atualizados!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Configuração da interface
app = tk.Tk()
app.title("Processamento de Currículos Lattes")
app.geometry("650x450")  # Tamanho adequado para caber todos os elementos

# Usar tema "clam" do ttk para modernizar a interface
style = ttk.Style()
style.theme_use('clam')

# Variáveis
entrada_arquivo = tk.StringVar()
saida_pasta = tk.StringVar()
formato_var = tk.StringVar(value="excel")
tipo_saida_var = tk.StringVar(value="detalhado")

# Layout usando ttk para uma aparência mais moderna
frame_arquivo = ttk.Frame(app, padding="10 10 10 10")
frame_arquivo.pack(fill="x", pady=10)
ttk.Label(frame_arquivo, text="Selecione o arquivo XML", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
ttk.Entry(frame_arquivo, textvariable=entrada_arquivo, width=40).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Button(frame_arquivo, text="Selecionar Arquivo", command=selecionar_arquivo).grid(row=1, column=1, padx=10)

frame_pasta = ttk.Frame(app, padding="10 10 10 10")
frame_pasta.pack(fill="x", pady=10)
ttk.Label(frame_pasta, text="Selecione a pasta de destino", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
ttk.Entry(frame_pasta, textvariable=saida_pasta, width=40).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Button(frame_pasta, text="Selecionar Pasta", command=selecionar_pasta_destino).grid(row=1, column=1, padx=10)

frame_formato = ttk.Frame(app, padding="10 10 10 10")
frame_formato.pack(fill="x", pady=10)
ttk.Label(frame_formato, text="Escolha o formato de saída", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
ttk.Radiobutton(frame_formato, text="Excel", variable=formato_var, value="excel").grid(row=1, column=0, sticky="w")
ttk.Radiobutton(frame_formato, text="JSON", variable=formato_var, value="json").grid(row=1, column=1, sticky="w")

frame_tipo_saida = ttk.Frame(app, padding="10 10 10 10")
frame_tipo_saida.pack(fill="x", pady=10)
ttk.Label(frame_tipo_saida, text="Escolha o tipo de geração", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
ttk.Radiobutton(frame_tipo_saida, text="Detalhado", variable=tipo_saida_var, value="detalhado").grid(row=1, column=0, sticky="w")
ttk.Radiobutton(frame_tipo_saida, text="Resumo", variable=tipo_saida_var, value="resumo").grid(row=1, column=1, sticky="w")

# Botão de execução moderno
ttk.Button(app, text="Executar", command=executar_processamento, style="TButton").pack(pady=20)

# Executar a aplicação
app.mainloop()
