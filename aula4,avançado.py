while True:
    try:
        idade=int(input("qual é sua idade: "))
        if idade < 0:
            print("idade não pode ser negativa")
            continue
        elif idade > 120:
            print("do que vc é feito?")
            break
        else:
            print("idade válida para acesso")
            break

    except ValueError:
        print("digite apenas numeros")

while True:
    try:
        ingresso=input(" possui um ingresso: ")
        if ingresso.lower() not in ["sim", "não", "nao"]:
            print("resposta inválida, digite 'sim' ou 'não'")
            continue
        else:
            print("resposta válida para ingresso")
            break

    except ValueError:
        print("digite apenas 'sim' ou 'não'")

if idade <=17:
    print("acesso negado, idade minima de entrada é 18")
    status = "negado"

elif idade >= 18 and ingresso.lower() == "sim":
    print("acesso permitido, aproveite a festa")
    status = "permitido"

else:
    print("acesso negado, deve comprar um ingresso para entrar")
    status = "pendente"

if status == "negado":
    print("vc não tem idade suficiente para entrar")

elif status == "permitido":
    print("vc pode entrar")

else: 
    print("vc precisa comprar um ingresso para entrar")