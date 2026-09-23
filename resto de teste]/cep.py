import tkinter as tk
from tkinter import messagebox
import requests


def consultar_cep():
    """
    Consulta um CEP informado pelo usuário utilizando a API ViaCEP
    e apresenta o resultado na interface gráfica.
    """

    # Obtém o CEP digitado e remove espaços e hífen
    cep = entrada_cep.get().strip().replace("-", "")

    # Validação básica: o CEP deve possuir 8 dígitos numéricos
    if not cep.isdigit() or len(cep) != 8:
        messagebox.showwarning(
            "CEP inválido",
            "Informe um CEP com 8 números.\nExemplo: 01001000 ou 01001-000."
        )
        return

    # Monta dinamicamente a URL da API
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # Faz a chamada HTTP para o ViaCEP
        resposta = requests.get(url, timeout=10)

        # Gera uma exceção caso a requisição HTTP tenha falhado
        resposta.raise_for_status()

        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()

        # O ViaCEP retorna {"erro": true} quando o CEP não existe
        if dados.get("erro"):
            limpar_resultado()
            messagebox.showinfo(
                "CEP não encontrado",
                "O CEP informado não foi encontrado."
            )
            return

        # Apresenta os dados retornados pela API
        valor_cep.config(text=dados.get("cep", ""))
        valor_logradouro.config(text=dados.get("logradouro", ""))
        valor_bairro.config(text=dados.get("bairro", ""))
        valor_cidade.config(text=dados.get("localidade", ""))
        valor_uf.config(text=dados.get("uf", ""))

        label_status.config(text="Status: consulta realizada com sucesso.")

    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Tempo excedido",
            "A consulta demorou mais que o esperado."
        )
        label_status.config(text="Status: erro de timeout.")

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Erro de conexão",
            "Não foi possível conectar ao serviço ViaCEP.\nVerifique sua conexão com a Internet."
        )
        label_status.config(text="Status: erro de conexão.")

    except requests.exceptions.RequestException as erro:
        messagebox.showerror(
            "Erro na consulta",
            f"Ocorreu um erro ao consultar o CEP:\n{erro}"
        )
        label_status.config(text="Status: falha na consulta.")

    except ValueError:
        messagebox.showerror(
            "Resposta inválida",
            "O serviço retornou uma resposta que não pôde ser interpretada."
        )
        label_status.config(text="Status: resposta inválida.")


def limpar_resultado():
    """Limpa os campos de resultado da interface."""
    valor_cep.config(text="")
    valor_logradouro.config(text="")
    valor_bairro.config(text="")
    valor_cidade.config(text="")
    valor_uf.config(text="")
    label_status.config(text="Status: aguardando consulta.")


def limpar_tela():
    """Limpa o CEP digitado e todos os dados apresentados."""
    entrada_cep.delete(0, tk.END)
    limpar_resultado()
    entrada_cep.focus()


# ---------------------------------------------------------
# CRIAÇÃO DA INTERFACE GRÁFICA
# ---------------------------------------------------------

janela = tk.Tk()
janela.title("RPA com Python - Consulta de CEP")
janela.geometry("520x400")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="CONSULTA AUTOMÁTICA DE CEP",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=15)

# Área de entrada
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=5)

label_cep = tk.Label(frame_entrada, text="CEP:", font=("Arial", 11))
label_cep.grid(row=0, column=0, padx=5)

entrada_cep = tk.Entry(frame_entrada, width=20, font=("Arial", 11))
entrada_cep.grid(row=0, column=1, padx=5)
entrada_cep.focus()

botao_consultar = tk.Button(
    frame_entrada,
    text="CONSULTAR CEP",
    command=consultar_cep,
    width=16
)
botao_consultar.grid(row=0, column=2, padx=5)

# Área de resultados
frame_resultado = tk.LabelFrame(
    janela,
    text="Resultado da consulta",
    padx=15,
    pady=15
)
frame_resultado.pack(fill="x", padx=30, pady=15)

campos = [
    ("CEP:", 0),
    ("Logradouro:", 1),
    ("Bairro:", 2),
    ("Cidade:", 3),
    ("UF:", 4)
]

for texto, linha in campos:
    tk.Label(
        frame_resultado,
        text=texto,
        font=("Arial", 10, "bold"),
        anchor="w"
    ).grid(row=linha, column=0, sticky="w", pady=4)

valor_cep = tk.Label(frame_resultado, text="", anchor="w")
valor_cep.grid(row=0, column=1, sticky="w", padx=10)

valor_logradouro = tk.Label(frame_resultado, text="", anchor="w")
valor_logradouro.grid(row=1, column=1, sticky="w", padx=10)

valor_bairro = tk.Label(frame_resultado, text="", anchor="w")
valor_bairro.grid(row=2, column=1, sticky="w", padx=10)

valor_cidade = tk.Label(frame_resultado, text="", anchor="w")
valor_cidade.grid(row=3, column=1, sticky="w", padx=10)

valor_uf = tk.Label(frame_resultado, text="", anchor="w")
valor_uf.grid(row=4, column=1, sticky="w", padx=10)

# Botão para limpar
botao_limpar = tk.Button(
    janela,
    text="LIMPAR",
    command=limpar_tela,
    width=15
)
botao_limpar.pack(pady=5)

# Status
label_status = tk.Label(
    janela,
    text="Status: aguardando consulta.",
    font=("Arial", 9, "italic")
)
label_status.pack(pady=10)

# Permite consultar pressionando Enter
janela.bind("<Return>", lambda event: consultar_cep())

# Inicia a aplicação
janela.mainloop()