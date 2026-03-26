senha = input("Crie uma senha: ")

while True:
    confirmar = input("Confirme sua senha: ")
    if(confirmar == senha):
        print("Senha criada com sucesso")
        break