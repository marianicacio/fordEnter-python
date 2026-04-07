pessoas = 0
qtd_pessoas = 0
bloqueadas = 0
entradasTotal = 0
entradasS = 0
pessoas = int(input("Quantas pessoas vão entrar no evento: "))

while pessoas > 0:
    if(pessoas == qtd_pessoas):
        break
    idade = int(input("idade: "))
    if(idade >= 18):
        print("Passou")
        entradasS += 1
        entradasTotal += 1
    elif(idade <= 17 and idade >= 16):
        convite = input("Tem convite: ")
        if(convite == "sim"):
            print("Passou")
            entradasTotal += 1
        elif(convite == "não"):
            print("Bloqueado")
            bloqueadas += 1
        else:
            print("Inválido")
    else:
        print("Bloqueado") 
        bloqueadas += 1       
    qtd_pessoas += 1

print(f"Entraram: {entradasTotal}")
print(f"Entraram sem convite: {entradasS}")
print(f"Pessoas barradas: {bloqueadas}")
    