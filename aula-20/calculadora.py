# Calculadora que recebe dois numeros e me entrega os resultaos de some, subtração,divisão, multiplicação, expoente e resto

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
opcao = int(input(" Digite o número da opção desejada  \n" \
"1. Adição\n" \
"2. Subtração\n" \
"3. Divisão\n" \
"4. Multiplicação\n" \
"5. Restante de divisão\n" \
"6. Expoente\n" \
))

erro = False

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
exp = n1 ** n2


if(opcao == 1):
    print(f"Soma: {n1} + {n2} = {soma}")
elif(opcao == 2):
    print(f"Subtração: {n1} - {n2} = {sub}")
elif(opcao == 3):

    if(n1 == 0 or n2 == 0):
        print("Não é possível dividir por 0")
        erro = True
    else: 
        result = n1 / n2
        print(result)

elif(opcao == 4):
    print(f"Multiplicação: {n1} * {n2} = {mult}")
elif(opcao == 5):

    if(n1 == 0 or n2 == 0):
        print("Não é possível dividir por 0")
        erro = True
    else: 
        print("Seu número é: ")

    print(f"O resultado do resto: {n1 % n2}" )

#Realizando a verificação do n1
    if (n1 % 2 == 0): 
        print(f"{n1} é par")
    else:
        print(f"{n1} é impar")

#Realizando a verificação do n2
    if (n2 % 2 == 0): 
        print(f"{n2} é par")
    else:
        print(f"{n2} é impar")
         
   

elif(opcao == 6):
    print(f"Expoente: {n1} ** {n2} = {exp}")
else:
    print("Opção recusada!!")


# print(n1, "+" , n2, "=", soma) : tbm funciona