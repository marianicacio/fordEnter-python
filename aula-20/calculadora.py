# Calculadora que recebe dois numeros e me entrega os resultaos de some, subtração,divisão, multiplicação, expoente e resto

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o primeiro número: "))
soma = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
exp = n1 ** n2
resto = n1 % n2

# print(n1, "+" , n2, "=", soma) : tbm funciona
print(f"Soma: {n1} + {n2} = {soma}")
print(f"Subtração: {n1} - {n2} = {sub}")
print(f"Divisão: {n1} / {n2} = {div}")
print(f"Multiplicação: {n1} * {n2} = {mult}")
print(f"Expoente: {n1} ** {n2} = {exp}")
print(f"Resto: {n1} % {n2} = {resto}")

if (n1 % 2 == 0): 
    print(f"{n1} número é divido por 2")
else:
    print(f"{n1} número é impar2")

if (n2 % 2 == 0): 
    print(f"{n2} número é divido por 2")
else:
    print(f"{n2} número é impar")
     
