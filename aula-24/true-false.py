#or

camiseta = 5500.50
calca  = 690.90
saldo = 500.00
credito = 1000.00
total = saldo + credito

opcao_compra = input('1 - camiseta \n' \
'2 - calça \n'
)

if(opcao_compra == "1"):
    if(saldo >= camiseta or credito >= camiseta or total >= camiseta):
        print("Parabens pela compra!!")

elif(opcao_compra == "2"):
    if(saldo >= calca or credito >= calca or total >= calca):
        print("Parabens pela compra!!")