for i in range(100):
    nome = input("Digite seu nome: ")
    senha = input("Crie uma senha: ")
    if(nome != senha):
        print("Cadastro realizado com sucesso!")
        break
    else:
       print("Nome e senha não pode ser igual, tente novamente!")
else: 
    print("Limite atingido")