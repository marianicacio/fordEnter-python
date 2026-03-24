nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
tempoT = input("Digite quantos anos foi trabalhado: ")

if(salario <= 3000 and tempoT >= "2"):
    print("bônus concedido")
else:
    print("bônus não foi concedido")