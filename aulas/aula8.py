import random

## nome fixos no array
array_nomes =["Alice","Bruno", "Carla", "Gabriel", "Daniela", "Eduardo",
               "Fernanda", "Gustavo", "Helena", "Igor"]
lista_aleatoria = array_nomes.copy()
random.shuffle(lista_aleatoria)

print("Lista de nomes aleatória:")
print("\n")
for nome in lista_aleatoria:
    print(nome)

nome_escolhido = input("\nDigite o nome que deseja buscar na lista original:").strip()

def buscar_nome(array, nome):
    for posicao in range(len(array)):
        if array[posicao].lower() == nome.lower():
            return posicao

    return -1

posicao = buscar_nome(array_nomes, nome_escolhido)

if posicao != -1:
    print(f"\nO nome encontrado: {array_nomes[posicao]}")
    print(f"Posição do nome na lista original: {posicao}")

else:
    print("\nNome não encontrado na lista original.")
