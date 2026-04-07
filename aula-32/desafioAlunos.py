aluno ={
    'nome': '',
    'idade': '',
    'curso': '',
}

aluno['nome'] = input("Digite seu nome: ")
aluno['idade'] = input("Digite sua idade: ")
aluno['curso'] = input("Digite seu curso: ")
aluno['nota'] = int(input("Digite sua nota: "))

print(f"Nome do aluno: {aluno['nome']}")
print(f"Idade do aluno: {aluno['idade']}")
print(f"Curso do aluno: {aluno['curso']}")
print(f"Nota do aluno: {aluno['nota']}")
