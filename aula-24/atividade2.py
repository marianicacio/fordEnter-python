nome = input("Digite seu nome: ")
notaFinal = float(input("Digite sua nota final: "))
frequencia = input("Digite sua frequencia em porcentagem: ")

if(notaFinal >= 7 or frequencia >= "75%"):
    print("Aprovado")
else:
    print("Reprovado")
