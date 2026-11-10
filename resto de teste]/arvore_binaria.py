
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


# Função para inserir elementos
def inserir(raiz, valor):

    if raiz is None:
        return No(valor)

    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)

    elif valor > raiz.valor:
        raiz.direita = inserir(raiz.direita, valor)

    return raiz


# Função para mostrar os elementos em ordem crescente
def mostrar(raiz):

    if raiz is not None:
        mostrar(raiz.esquerda)
        print(raiz.valor)
        mostrar(raiz.direita)


# Função para pesquisar um número
def pesquisar(raiz, valor):

    if raiz is None:
        return False

    if raiz.valor == valor:
        return True

    if valor < raiz.valor:
        return pesquisar(raiz.esquerda, valor)

    else:
        return pesquisar(raiz.direita, valor)


# Função para contar os nós
def contar_nos(raiz):

    if raiz is None:
        return 0

    return 1 + contar_nos(raiz.esquerda) + contar_nos(raiz.direita)


# Função para encontrar o maior valor
def maior_valor(raiz):

    if raiz is None:
        return None

    while raiz.direita is not None:
        raiz = raiz.direita

    return raiz.valor


# Função para encontrar o menor valor
def menor_valor(raiz):

    if raiz is None:
        return None

    while raiz.esquerda is not None:
        raiz = raiz.esquerda

    return raiz.valor

def desenhar_arvore(raiz, nivel=0, lado="RAIZ"):

    if raiz is not None:

        print("    " * nivel + f"└── {raiz.valor} ({lado})")

        desenhar_arvore(raiz.esquerda, nivel + 1, "ESQ")
        desenhar_arvore(raiz.direita, nivel + 1, "DIR")

# Programa principal
raiz = None

while True:

    print("\n===== ÁRVORE BINÁRIA =====")
    print("1 - Inserir número")
    print("2 - Mostrar números")
    print("3 - Pesquisar número")
    print("4 - Contar elementos")
    print("5 - Mostrar maior número")
    print("6 - Mostrar menor número")
    print("0 - Sair")
    print("7 - Desenhar árvore")

    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:

            valor = int(input("Digite o número que deseja inserir: "))
            raiz = inserir(raiz, valor)

            print("Número inserido com sucesso!")

        elif opcao == 2:

            if raiz is None:
                print("A árvore está vazia!")
            else:
                print("\nNúmeros armazenados:")
                mostrar(raiz)

        elif opcao == 3:

            valor = int(input("Digite o número que deseja pesquisar: "))

            if pesquisar(raiz, valor):
                print("Número encontrado!")
            else:
                print("Número não encontrado!")

        elif opcao == 4:

            print(f"Quantidade de elementos: {contar_nos(raiz)}")

        elif opcao == 5:

            resultado = maior_valor(raiz)

            if resultado is None:
                print("A árvore está vazia!")
            else:
                print(f"Maior número: {resultado}")

        elif opcao == 6:

            resultado = menor_valor(raiz)

            if resultado is None:
                print("A árvore está vazia!")
            else:
                print(f"Menor número: {resultado}")

        elif opcao == 0:

            print("Encerrando o programa...")
            break

        elif opcao == 7:

            if raiz is None:
             print("A árvore está vazia!")
            else:
             print("\nVisualização da árvore:")
             desenhar_arvore(raiz)

        else:
            print("Opção inválida!")

    except ValueError:
        print("Digite apenas números inteiros!")






