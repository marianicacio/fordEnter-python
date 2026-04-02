pessoas = int(input("Digite a quantidade de pessoas: "))
qtd_pessoas = 0
qtd_beta = 0
qtd_alfa = 0
qtd_z = 0
qtd_y = 0
qtd_x = 0
qtd_babyB = 0
qtd_silent = 0

for i in range(1, pessoas + 1, 1):
    idade = int(input(f"Digite a idade da pessoa {qtd_pessoas}: "))
    if(idade == 0 or idade <= 1):
        print("Geração Beta")
        qtd_beta += 1
    elif(idade >= 2 and idade <= 14):
        print("Geração Alfa")
        qtd_alfa += 1
    elif(idade >= 15 and idade <= 29):
        print("Geração Z")
        qtd_z += 1
    elif(idade >= 30 and idade <= 45):
        print("Geração Y")
        qtd_y += 1
    elif(idade >= 46 and idade <= 61):
        print("Geração X")
        qtd_x += 1
    elif(idade >= 62 and idade <= 80):
        print("Baby Boomers")
        qtd_babyB += 1
    elif(idade >= 81 and idade <= 101):
        print("Baby Boomers")
        qtd_silent += 1
    else:
        print("Valor inválido")
    qtd_pessoas = pessoas =+ 1

print(f"Quantidades de pessoas da geração betas: {qtd_beta}")
print(f"Quantidades de pessoas da geração alfas: {qtd_alfa}")
print(f"Quantidades de pessoas da geração z: {qtd_z}")
print(f"Quantidades de pessoas da geração x: {qtd_x}")
print(f"Quantidades de pessoas da geração y: {qtd_y}")
print(f"Quantidades de pessoas da geração baby boomers: {qtd_babyB}")
print(f"Quantidades de pessoas da geração silent: {qtd_silent}")