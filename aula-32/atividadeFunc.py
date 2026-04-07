nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = "Curso FIC Senai"

def apresentação(nome, idade, curso):
    print(f"O nome do aluno é {nome}, idade: {idade}, curso: {curso}")

apresentação(nome, idade, curso)