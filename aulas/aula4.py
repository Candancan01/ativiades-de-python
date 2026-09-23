print("\n" + "=" * 50)
print("   SEJA BEM VINDO A BALADA DO VENENO")
print("\n" + "=" * 50)

idade=int(input("qual é sua idade: "))
ingresso=input(" possui um ingresso: ")

if idade <= 16:
    print("vc não pode entrar")

elif idade >= 17 and ingresso=="sim":
    print("pode entrar")

else:
    print("compre um ingresso para entrar")