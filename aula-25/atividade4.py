numero = int(input("Digite um numero: "))
vezes = 0

while numero >= 1:
    numero /= 10
    vezes += 1

print(f"Casas decimais: {vezes}")