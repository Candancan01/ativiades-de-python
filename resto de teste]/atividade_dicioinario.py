produto = {
    "nome": "arroz",
    "preco": 5.99,
    "quantidade": 10
}


## dicionário salva em duplas, ou seja o parametro e o resultado
## diferente das tuplas, no dicionario vc pode alterar os valores


for chave, valor in produto.items():
    print(chave, ":", valor)
      ## essa linha de for serve para printar o dicionário com o parametro e resultado
        ## se usar print (produto) ele vai printar o dicionário inteiro
        ## se usar o print (produto["nome"]) ele vai printar apenas o parametro nome 

print("\n")
print("alterando os valores com o termo update")
print("\n")


produto.update({
    "preco": 6.50,
    "estoque": 15,
    "categoria": "Alimentos"
})

for chave, valor in produto.items():
    print(chave, ":", valor)


