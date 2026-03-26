turma = 0
alunos = 0 

qtd_turmas = 0

while True:
    turmas = int(input("Digite a quantidade das turmas: "))
    if(turmas == 0):
        break
    aluno = int(input("Digite a quantidade de alunos: "))
    if(aluno>40):
        print("Não é possivel ter mais de 40 alunos")

    qtd_alunos = alunos + aluno
    qtd_turmas += turmas

if (qtd_turmas > 0):
    media = qtd_alunos/qtd_turmas
    print(f"Quantidade de turmas: {qtd_turmas}")
    print(f"Média: {media:.2f}")