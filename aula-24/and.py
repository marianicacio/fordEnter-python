print("10 é maior que 5?", 10>5)
print(10<5)
print(10>=10)
print("a" == "a")
print("b" != "b")


# And
print(10>5 and 10==5) #false
login = "maria@gmail.com"
senha = "123"
entrada_login = input("Digite seu email: ")
entrada_senha = input("Digite sua senha: ")

if(login == entrada_login and entrada_senha == entrada_senha):
    print("Entrou")


else:
    print("Usúario inválido")
