turma = int(input("Digite a turma: "))
alunos = int(input("Digite a quantidade de alunos dessa turma: "))

if(alunos > 40):
      print("Alunos não pode ser maior que 40")

while alunos <= 40:
        turma = int(input("Digite a turmas (Digite 0 caso não tenha mais turmas): "))
        if(turma == 0):
            print("Finalizado")
            break
        alunos = int(input("Digite a quantidade de alunos: "))