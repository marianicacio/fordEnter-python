texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print()

for n1 in [8, 7, 17, 25, 38]:
    print(n1)

numero = [8, 7, 17, 25, 38]

for n1 in numero:
    print(n1)

numero = 5

for numero in range(10, 20, 3):
    print(numero)

"""
For comecou a contar pelo 10 até o numero 20 e de 3 em 3
"""

for i in range(1, 6, 2):
    print(1)

for i in range(1, 6):
    print(1)

for i in range(0, 4):
    print(i)
print("GO")

for n in range(10, -1, -1):
    print(n)

tabuada = int(input("Digite um numero: "))

for num in range(0, 11, 1):
    print(f"{num} X {tabuada} = {num * tabuada}")
else:
    print("Acabou")

for x in [1,10,20,30,40,50]:
    if x == 30:
        continue
    print(x)

for y in range(10000000000):
    print(y)
    if y == 150:
        break
print("Ate mais")