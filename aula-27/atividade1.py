pessoas = int(input("Digite a quantidade de pessoas: "))
qtd_pessoas = 0
feminino = 0
masculino = 0

for i in range(1, pessoas + 1, 1):
    genero = input("Essa pessoa é de que gênero? ")
    if(genero == "m"):
        masculino += 1
        print("Masculino")
    elif(genero == "f"):
        feminino += 1
        print("Feminino")
    else:
        print("Inválido")

    qtd_pessoas = genero =+ 1

print(f"Total de pessoas do gênero masculino: {masculino}")
print(f"Total de pessoas: {pessoas}")