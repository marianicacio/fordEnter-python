import pandas as pd

df = pd.read_excel("aula-36/vinhos_tratamento.xlsx")

media_populacao = df["volume_hl"].mean()
print(f"Média da população: {round(media_populacao, 2)}")

medias_amostras = []

for i in range(5):
    amostra = df.sample(frac=0.05)
    media_amostra = amostra["volume_hl"].mean()
    medias_amostras.append(media_amostra)

print("-" * 40)

for i, media in enumerate(medias_amostras):
    print(f"Amostra {i+1}: {round(media, 2)}")

    #As médias das amostras são próximas da média da população, mas apresentam pequenas variações entre si.