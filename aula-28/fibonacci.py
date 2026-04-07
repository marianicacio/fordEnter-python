numero = int(input("Digite um numero: "))
numero_inicial = 0
proximo = 1
soma = numero_inicial + proximo

print(numero_inicial)
print(proximo)
print(soma)
    

while soma < numero:
    
    numero_inicial = proximo
    proximo = soma
    soma = numero_inicial + proximo
    
    if(soma > numero):
        break
    
    print(soma)
    