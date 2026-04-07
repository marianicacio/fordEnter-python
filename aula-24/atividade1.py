idade = int(input("Digite sua idade: "))
autorizacao = input("Você tem autoziautorização dos responsáveis: \n" \
"Sim\n" \
"Não\n"
)

if(idade >= 18 or autorizacao == "Sim"):
    print("Acesso liberado")
else:
    print("Acesso negado")
