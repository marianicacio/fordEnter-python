def contar_pares(*n):
    for i in n:
        if(i % 2 == 0):
            print(f"O numero {i} é par")
        else:
            print("Impar")
contar_pares(9)