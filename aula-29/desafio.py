combustivel = input("Qual tipo de combustivel: \n A - alcool \n G - gasolina \n")
combustivel = combustivel.upper()
litros = float(input("Digite quantos litros deseja colocar: "))
precoA = 3.89
precoG = 5.50
precoTotalA = litros * precoA
precoTotalG = litros * precoG
descontoA = precoTotalA * 0.03
descontoAcimaA = precoTotalA * 0.05
descontoAcimaG = precoTotalA * 0.06
descontoG = precoTotalA * 0.04

if(combustivel == "A"):
    if(litros <= 20): 
        print(f"Valor a ser pago: R${precoTotalA - descontoA:.2f}")
    else:
        print(f"Valor a ser pago: R${precoTotalA - descontoAcimaA:.2f}")

if(combustivel == "G"):
    if(litros <= 20): 
        print(f"Valor a ser pago: R${precoTotalG - descontoG:.2f}")
    else:
        print(f"Valor a ser pago: R${precoTotalG - descontoAcimaG:.2f}")
else:
    print("Valor inválido")