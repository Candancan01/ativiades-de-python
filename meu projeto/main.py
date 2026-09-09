from produto import produto
from estoque import estoque

p1 = produto("PS5", 5000, 10)
p2 = produto("iPhone 13", 2500, 5)
p3 = produto("Fone de ouvido", 15, 50)

estoque = estoque()
estoque.adicionar(p1)
estoque.adicionar(p2)
estoque.adicionar(p3)

estoque.listar()

p1.vender(3)
print(f"Quantidade restante de PS5: {p1.quantidade}")
