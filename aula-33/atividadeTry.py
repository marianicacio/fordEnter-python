try:
    def divisao_save(a,b):
        res = a/b 
        print(f"Resultado da divisão: {res}")
    divisao_save(3,2)
except ZeroDivisionError:
    print("Não é possivel dividir por 0")


        