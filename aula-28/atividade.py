idades = []
alturas = []

for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    altura = int(input(f"Digite a altura do aluno {i+1}: "))

    idades.append(idade)
    idades.append(alturas)
    
    media = sum(alturas) / len(alturas)
    
    contador = 0
    
for i in range(30):
    if(idade[i] > 13 and alturas[i] < media):
         contador += 1

print(f"{contador} alunos com mais de 13 anos têm altura abaixo da média.")

