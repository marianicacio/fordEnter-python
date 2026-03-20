nota1 = float(input("Nota do primeiro Semestre: "))
nota2 = float(input("Nota do primeiro Semestre: "))
nota3 = float(input("Nota do primeiro Semestre: "))

media = (nota1 + nota2 + nota3)/3

if(media >= 7):
    print(f"Passou de ano: {media}")
elif(media >= 5 or media < 7):
    print(f"Recuperação: {media}")
else:
    print(f"Reprovado: {media}")


