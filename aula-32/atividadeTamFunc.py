palavra = input("Digite uma palavra: ")

def tamanha_palavra(palavra):
    tamanho = 0
    for i in palavra:
        tamanho += 1
        print(tamanho)

tamanha_palavra(palavra)