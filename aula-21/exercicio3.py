estadoCivil = input("Digite seu estado civil: \n"\
"C - Casado \n" \
"S - Solteiro \n" \
"D - Divorciado \n" \
"V - Viuvo \n" \
"O - Outro \n")

estadoCivil = estadoCivil.upper()

if(estadoCivil == "C"):
    print("C - Casado")
elif(estadoCivil == "S"):
    print("S - Solteiro")
elif(estadoCivil == "D"):
    print("D - Divorciado")
elif(estadoCivil == "V"):
    print("V - Viuvo")
elif(estadoCivil == "O"):
    print("O - Outro")
else:
    print("Opção inválida")