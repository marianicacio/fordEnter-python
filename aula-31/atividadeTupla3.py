#3.Crie uma tupla números = (5, 10, 15, 20) e converta-a em uma lista. Adicione o número 25 à lista resultante depois volte a lista para tupla e print ela.

numeros = (5, 10, 15, 20)

list_numeros = list(numeros)
list_numeros = list_numeros + [25]
tuple_numeros = tuple(list_numeros)

print(tuple_numeros)