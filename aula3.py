print("\n" + "=" * 50)
print("         Seja bem vindo ao carrinho de compras         ")
print("=" * 50)

nome=input("qual é nome: ")
produto=input("Qual é o produto que vc está comprando: ")
preco=float(input("preço do produto: "))
quantidade=int(input("quantos produtos vc está comprando: "))
percentual_desconto=int(input("quanto de desconto está este produto: "))

subtotal= preco * quantidade
desconto= subtotal * (percentual_desconto / 100)
total_final = subtotal - desconto
valor_medio = total_final/ quantidade

print("\n" + "=" * 50)
print("         Recibo formatado         ")
print("=" * 50)

print (f'Nome do cliente: {nome}')
print (f'Produto: {produto}')
print (f'Preço unitário: R$ {preco:.2f}')
print (f'Quantidade: {quantidade}')
print (f'Percentual de desconto: {percentual_desconto}%')
print (f'Subtotal: R$ {subtotal:.2f}')
print (f'Desconto: R$ {desconto:.2f}')
print (f'Total final: R$ {total_final:.2f}')
print (f'Valor médio por produto: R$ {valor_medio:.2f}')

print("\n" + "=" * 50)
print("          OBRIGADO PELA COMPRA!          ")
print("=" * 50)