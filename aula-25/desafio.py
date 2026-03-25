idade = input("Digite sua idade: ")

while True:
    try:
        diaNascimento = int(input("Digite o dia que vc nasceu: "))
        if(diaNascimento <= 0 or diaNascimento > 31):
            print("Nasceu como filho?")
        else:
            break
    except ValueError:
        print("Nasceu como filho?")

while True:
    try:
        mesNascimento = int(input("Digite o mes que vc nasceu: "))
        if(mesNascimento <= 0 or mesNascimento > 12):
            print("Nasceu como filho?")
        else:
            break
    except ValueError:
        print("Nasceu como filho?")

if(idade <= "12"):
    print("Criança")
elif(idade >= "13" and idade <= "17"):
    print("Adolescente")
elif(idade >= "18" and idade <= "25"):
    print("Adulto J")
elif(idade >= "26" and idade <= "35"):
    print("Adulto R")
elif(idade >= "36" and idade <= "60"):
    print("Adulto Sr")
else: 
    print("Idoso")

if(mesNascimento == 12 or mesNascimento == "Dezembro"):
    if(diaNascimento >= 22):
        print("Capricornio")
    else:
        print("Sargitario")

if(mesNascimento == 1 or mesNascimento == "Janeiro"):
    if(diaNascimento >= 19):
        print("Aquario")
    else:
        print("Capricornio")

if(mesNascimento == 2 or mesNascimento == "Fevereiro"):
    if(diaNascimento >= 19):
        print("Peixes")
    else:
        print("Aquário")

if(mesNascimento == 3 or mesNascimento == "Março"): 
    if(diaNascimento >= 21):
        print("Áries")
    else:
        print("Peixes")

if(mesNascimento == 4 or mesNascimento == "Abril"):
    if(diaNascimento >= 20):
        print("Touro")
    else:
        print("Áries")

if(mesNascimento == 5 or mesNascimento == "Maio"):
    if(diaNascimento >= 21):
        print("Gêmeos")
    else:
        print("Touro")

if(mesNascimento == 6 or mesNascimento == "Junho"):
    if(diaNascimento >= 21):
        print("Câncer")
    else:
        print("Touro")

if(mesNascimento == 7 or mesNascimento == "Julho"):
    if(diaNascimento >= 23):
        print("Leão")
    else:
        print("Câncer")

if(mesNascimento == 8 or mesNascimento == "Agosto"):
    if(diaNascimento >= 23):
        print("Virgem")
    else:
        print("Leão")

if(mesNascimento == 9 or mesNascimento == "Setembro"):
    if(diaNascimento >= 23):
        print("Libra")
    else:
        print("Virgem")

if(mesNascimento == 10 or mesNascimento == "Outubro"):
    if(diaNascimento >= 23):
        print("Escorpião")
    else:
        print("Libra")

if(mesNascimento == 11 or mesNascimento == "Novembro"):
    if(diaNascimento >= 22):
        print("Sagitário")
    else: 
        print("Escorpião")


