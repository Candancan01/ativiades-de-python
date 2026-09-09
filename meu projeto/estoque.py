class estoque:
## (def __init__) serve para rodar de forma automática quando a classe é usada
    ## fazendo um def na qual cria uma lista de produtos
    def __init__(self):
        self.produtos = []


## fazedno um def na qual adiciona produtos na lista de produtos
    def adicionar(self, produto):
 ## essa parte serve para adicionar o produto escolhido como o ultimo novo item da lista
        self.produtos.append(produto)
        print(f"produto {produto.nome} adicionado ao estoque com sucesso! \n")


    def listar(self):
        print("produtos em estoque:")
        for produto in self.produtos:
            print(f"Item: {produto.nome} \n Preço: R${produto.preco} \n Quantidade: {produto.quantidade}\n \n")
