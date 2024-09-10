import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from main import processar_arquivo_xml  # Função que processa os arquivos XML

# Função para selecionar arquivo XML
def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo XML", filetypes=[("Arquivos XML", "*.xml")])
    if caminho_arquivo:
        entrada_arquivo.set(caminho_arquivo)

# Função para selecionar pasta de destino
def selecionar_pasta_destino():
    pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")
    if pasta_destino:
        saida_pasta.set(pasta_destino)

# Função para processar o arquivo
def executar_processamento():
    arquivo_xml = entrada_arquivo.get()
    pasta_saida = saida_pasta.get()
    formato_saida = formato_var.get()
    tipo_saida = tipo_saida_var.get()

    if not arquivo_xml or not pasta_saida:
        messagebox.showwarning("Campos obrigatórios", "Por favor, selecione o arquivo XML e a pasta de destino.")
        return

    try:
        processar_arquivo_xml(arquivo_xml, formato_saida, pasta_saida, tipo_saida)
        messagebox.showinfo("Sucesso", "Arquivo processado com sucesso e dados detalhados/gerais atualizados!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Configuração da interface
app = tk.Tk()
app.title("Processamento de Currículos Lattes")

# Estilo customizado para modernizar a interface
style = ttk.Style(app)
style.theme_use('clam')

# Definir algumas cores e fontes para uma interface moderna
style.configure('TFrame', background='#2C3E50')  # Cor de fundo para os frames
style.configure('TLabel', background='#2C3E50', foreground='white', font=('Arial', 12))
style.configure('TButton', background='#18BC9C', foreground='#3d756a', font=('Arial', 10, 'bold'))
style.configure('TRadiobutton', background='#2C3E50', foreground='white', font=('Arial', 11))

app.geometry("500x400")
app.configure(background='#2C3E50')  # Cor de fundo da janela principal

# Variáveis
entrada_arquivo = tk.StringVar()
saida_pasta = tk.StringVar()
formato_var = tk.StringVar(value="excel")
tipo_saida_var = tk.StringVar(value="detalhado")

# Layout principal
frame_principal = ttk.Frame(app, padding="20 20 20 20")
frame_principal.pack(fill="both", expand=True)

# Seção para selecionar o arquivo XML
frame_arquivo = ttk.Frame(frame_principal)
frame_arquivo.grid(row=0, column=0, sticky="w", pady=10)
ttk.Label(frame_arquivo, text="Selecione o arquivo XML").grid(row=0, column=0, sticky="w")
ttk.Entry(frame_arquivo, textvariable=entrada_arquivo, width=35).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Button(frame_arquivo, text="Selecionar Arquivo", command=selecionar_arquivo).grid(row=1, column=1, padx=10)

# Seção para selecionar a pasta de destino
frame_pasta = ttk.Frame(frame_principal)
frame_pasta.grid(row=1, column=0, sticky="w", pady=10)
ttk.Label(frame_pasta, text="Selecione a pasta de destino").grid(row=0, column=0, sticky="w")
ttk.Entry(frame_pasta, textvariable=saida_pasta, width=35).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Button(frame_pasta, text="Selecionar Pasta", command=selecionar_pasta_destino).grid(row=1, column=1, padx=10)

# Seção para escolher o formato de saída (Excel ou JSON)
frame_formato = ttk.Frame(frame_principal)
frame_formato.grid(row=2, column=0, sticky="w", pady=10)
ttk.Label(frame_formato, text="Escolha o formato de saída").grid(row=0, column=0, sticky="w")
ttk.Radiobutton(frame_formato, text="Excel", variable=formato_var, value="excel").grid(row=1, column=0, sticky="w")
ttk.Radiobutton(frame_formato, text="JSON", variable=formato_var, value="json").grid(row=1, column=1, sticky="w")

# Seção para escolher o tipo de saída (Detalhado ou Resumo)
frame_tipo_saida = ttk.Frame(frame_principal)
frame_tipo_saida.grid(row=3, column=0, sticky="w", pady=10)
ttk.Label(frame_tipo_saida, text="Escolha o tipo de geração").grid(row=0, column=0, sticky="w")
ttk.Radiobutton(frame_tipo_saida, text="Detalhado", variable=tipo_saida_var, value="detalhado").grid(row=1, column=0, sticky="w")
ttk.Radiobutton(frame_tipo_saida, text="Resumo", variable=tipo_saida_var, value="resumo").grid(row=1, column=1, sticky="w")

# Botão de execução com estilo moderno
ttk.Button(app, text="Executar", command=executar_processamento).pack(pady=20)

# Executar a aplicação
app.mainloop()
