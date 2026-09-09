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

        case 2:
         print("termo de uso:")
         print("1. o usuário deve respeitar as regras do sistema")
         print("2. o usuário deve fornecer informações precisas e verdadeiras")

        case 3:
         print("saindo do sistema...")
         break

        case _:
            print("opção inválida, tente novamente")
        