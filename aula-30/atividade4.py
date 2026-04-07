pessoas = int(input("Digite a quantidade de pessoas: "))
masculino = 0
feminino = 0
idadeF = 0
idadeM = 0

for i in range(1, pessoas + 1, 1):
    genero = input("Digite o genero: \n F - Feminino \n M - Masculino \n")
    genero = genero.upper()
    if(genero == "F"):
        print("Gênero Feminino")
        idadeF = int(input("Digite sua idade: "))
        feminino += 1
    elif(genero == "M"):
        print("Gênero Masculino")
        idadeM = int(input("Digite sua idade: "))
        masculino += 1
    else:
        print("Outro")

mediaF = idadeF / feminino
mediaM = idadeM / masculino
media = idadeF + idadeM / pessoas


print(f"Quantidade de pessoas: {pessoas}")
print(f"Media idade Feminina: {mediaF}")
print(f"Media idade Masculina: {mediaM}")
print(f"Media total: {media}")
print(f"Quantidade de gêneros femininos: {feminino}")
print(f"Quantidade de gêneros masculinos: {masculino}")