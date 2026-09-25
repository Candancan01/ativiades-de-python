print("calculadora basica, sendo possivel fazer operações basicas")
print("apenas dois numeros por vez")
print("\n")

def somar(a,b):
    return a +b 

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a/b

while True:

    
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. sair")
    operacao= input("Digite a operação desejada: ")
    if operacao == "5":
        print("Saindo...")
        break
    n1= float(input("Digite o primeiro numero: "))
    n2= float(input("Digite o segundo numero: "))

    if operacao == "1":
        print(somar(n1, n2))
    elif operacao == "2":
        print(subtrair(n1, n2))
    elif operacao == "3":
        print(multiplicar(n1, n2))
    elif operacao == "4":
        if n2 == 0 or n1==0:
         print("Erro: Divisão por zero não é permitida.")
        else:
            print(dividir(n1, n2))
    else:
        print("Operação inválida!") 