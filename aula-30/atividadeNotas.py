soma = 0
media = 0

for i in range(4):
    numero = float(input("Digite um numero: "))
    soma = soma + numero
    media = soma / 4
print(f"Soma é: {soma}")
print(f"Media é: {media}")