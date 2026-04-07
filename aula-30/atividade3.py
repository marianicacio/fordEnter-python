eleitores = int(input("Digite a quantidade de eleitores: "))
qtd_eleitores = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(1, eleitores + 1, 1):
    voto = int(input(f"Digite seu voto eleitor {qtd_eleitores}: \n 1 - candidato 1 \n 2 - candidato 2 \n 3 - candidato 3 \n"))
    if(voto == 1):
        print("Votou em candidato 1")
        candidato1 += 1
    elif(voto == 2):
        print("Votou em candidato 2")
        candidato2 += 1
    elif(voto == 3):
        print("Votou em candidato 3")
        candidato3 += 1
    qtd_eleitores = eleitores =+ 1

print(f"Votos no candidato 1: {candidato1}")
print(f"Votos no candidato 1: {candidato2}")
print(f"Votos no candidato 1: {candidato3}")
