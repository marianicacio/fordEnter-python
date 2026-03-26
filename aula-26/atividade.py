pessoas = 0
qtd_pessoas = 0
pessoas = int(input("Quantas pessoas vão entrar no evento: "))

while pessoas > 0:
    idade = int(input("idade: "))
    if (idade >= 18):
         print("Entrou")
    elif(idade < 18 and idade >= 16):
         convite = input("Essa pessoa possui convite: ")
    elif(convite == "sim"):
         print("Entrou com sucesso")
    else:
         print("Bloqueado")
    qtd_pessoas = pessoas =+ 1