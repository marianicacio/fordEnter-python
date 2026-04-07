from validate_docbr import CPF

nomeAluno = input("Qual seu nome: ")
print ("Seja muito bem-vindo!! " + nomeAluno)

cpf = CPF()

entrada = input("Antes de começar, entre com seu cpf: ")

if(cpf.validate(entrada)):
    print("Entrou com sucesso!")
else:
    print("CPF invalido")

"""
Gostei bastante de como funciona a logica do python, acabei ficando curiosa sobre a verificação de cpf, entao baixei o pacote validate-docbr para fazer a verificação.
"""