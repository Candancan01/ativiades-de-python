class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    def vender (self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"Venda realizada com sucesso, qunatidade vendida: {quantidade}")
        else:
            print("quantidade indiponível em estoque")