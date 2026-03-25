numeros = 0
qts_numeros = 0

while True:
    numero = int(input("Digite um numero para ser somado: "))
    if(numero == 0):
        break
    numeros = numeros + numero
    qts_numeros =  qts_numeros + 1
print(f"Você digitou {qts_numeros}")
print(f"A soma total é {numeros}")