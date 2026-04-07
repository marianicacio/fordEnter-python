while True:
    try:
        nota = int(input("Digite uma nota de 0 até 10: "))
        if(nota >= 0 and nota <= 10):
            break
        else:
            print("Digite outro valor")
    except ValueError:
        print("Valor invalido")

# nota = float(input("Digite um valor: "))

# while nota < 0 or nota > 10:
#     nota = float(input("Digite um valor: "))
# print("valor valido")