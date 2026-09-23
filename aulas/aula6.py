print ("=" * 70)
print ("SEJA BEM VINDO AO SISTEMA")
print ("=" * 70)

def exemplo_contadora():
    print("\n")
    print ("=" * 70)
    print ("EXEMPLO DE CONTADORA (while)")
    print ("=" * 70)
    print("\n")
    print("exemplo de contadora de 1 a 10")
    contador = 1
    while contador <= 10:
        print(contador)
        contador +=1

def exemplo_acumuladora():
    print("\n")
    print ("=" * 70)
    print ("EXEMPLO DE ACUMULADORA (while)")
    print ("=" * 70)
    print("\n")
    print("exemplo de acumuladora de 1 a 10")
    acumulador = 0
    contador = 1
    while contador <= 10:
        acumulador += contador
        print(acumulador)
        contador +=1

def exemplo_for_range():
    print("\n")
    print ("=" * 70)
    print ("FOR COM RANGE")
    print ("=" * 70)
    print("\n")
    print("exemplo de for com range de 1 a 10")
    for i in range(1, 11):
        print(i)


def exemplo_for_lista():
    print("\n")
    print ("=" * 70)
    print ("EXEMPLO DE FOR COM LISTA")
    print ("=" * 70)
    print("\n")
    frutas =["maçã", "banana", "laranja", "uva"]
    for f in frutas:
        print(f)

def exemplo_laços_alinhados():
    print("\n")
    print ("=" * 70)
    print ("EXEMPLO DE LAÇOS ALINHASDOS (matriz)")
    print ("=" * 70)
    print("\n")
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print ("matriz 3x3:")
    for linha in range (3):
        for coluna in range (3):
            print(matriz[linha][coluna], end=" ")
        print()
     

while True:
    print("\n")
    print ("digite 1 para ir ao menu principal do sistema")
    print ("digite 2 para teste rapido de funcionalidades")
    print ("digite 3 para sair do sistema")
    print ("\n")
    try:
        opcao1=int(input("digite a opção desejada: "))
        if opcao1 <1:
            print("opção inválida, digite um número entre 1 e 3")
            continue
    except ValueError:
        print("opção inválida, tente novamente")
        continue
    if opcao1 == 1:
        print("\n")
        print ("=" * 70)
        print ("MENU PRINCIPAL DO SISTEMA")
        print ("=" * 70)
        print("\n")
        print ("seja bem vindo ao sistema ")
        print (" digite 1 para fazer login" , "\n", "digite 2 para termo de uso", "\n", "digite 3 para sair")
        print("\n")
        while True:
            try:
                opcao=int(input("digite a opção desejada: "))
                if opcao <1:
                    print("opção inválida, digite um número entre 1 e 3")
                    continue

            except ValueError:
                print("opção inválida, tente novamente")
                continue
            

            match opcao:
                case 1:
                 nome=input("digite seu nome: ")
                 email=input("digite seu email: ")
                 senha=input("digite sua senha: ")
                 print("login realizado com sucesso")
                 print("bem vindo ao sistema", nome)
                 print("\n")
                 continue

                case 2:
                 print("termo de uso:")
                 print("1. o usuário deve respeitar as regras do sistema")
                 print("2. o usuário deve fornecer informações precisas e verdadeiras")
                 continue

                case 3:
                 print("saindo do sistema...")
                 break

                case _:
                    print("opção inválida, tente novamente")
    elif opcao1 == 2:
        while True:
         print("\n")
         print ("=" * 70)
         print ("EXEMPLOS INDIVIDUAIS")
         print ("=" * 70)
         print("\n")
         print ("escolha qual opção deseja executar:")
         print ("1- contadora (while)")
         print ("2- acumuladora (while)")
         print ("3- for com range")
         print ("4- for com lista")
         print ("5 - laços alinhados (matriz)")
         print ("6- saida do menu principál")
         print("\n")
         opcao2=int(input("digite a opção desejada: "))

         if opcao2 == 6:
             print("saindo do menu de exemplos individuais...")
             break

         elif opcao2 == 1:
             exemplo_contadora()

         elif opcao2 == 2:
             exemplo_acumuladora()

         elif opcao2 == 3:
             exemplo_for_range()

         elif opcao2 == 4:
             exemplo_for_lista()

         elif opcao2 == 5:
             exemplo_laços_alinhados()

         else:
             print("opção inválida, tente novamente")
    elif opcao1 == 3:
        print("saindo do sistema...")
        break
       