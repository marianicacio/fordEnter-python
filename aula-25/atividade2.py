notas = 0
qts_notas = 0

while True:
    nota = float(input("Digite sua nota (-1 para sair)"))
    if (nota == -1):
        break
    notas = notas+nota
    qts_notas=qts_notas+1
if (qts_notas>0):
    media = notas/qts_notas
    print(f"Quantidade de notas: {qts_notas}")
    print(f"Média: {media:.2f}")
else:
    print("Finalizado")