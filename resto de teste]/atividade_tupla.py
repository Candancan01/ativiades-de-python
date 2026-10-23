
produto = ("arroz", 5.99, 10)

print("nome do produto:", produto[0])
print("preço do produto:", produto[1])
print("quantidade do produto:", produto[2])

estoque_atual = produto[2]

while estoque_atual > 0:
    print("estoque atual:", estoque_atual)

    quantidade = int(input("Digite quantas unidades deseja comprar: "))

    valor_total = produto[1] * estoque_atual
    print("Valor total do estoque atual:", f"R$ {valor_total:.2f}")

    if quantidade > 0 and quantidade <= estoque_atual:
        valor_compra = produto[1] * quantidade
        print("Valor da compra:", f"R$ {valor_compra:.2f}")

        estoque_atual = estoque_atual - quantidade
        print("Quantidade atual em estoque:", estoque_atual)

    else:
        print("Quantidade inválida ou indisponível em estoque")

print("Estoque esgotado")
