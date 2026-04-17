import pandas as pd

df = pd.read_csv("aula-36/vinhos.csv")

media_populacao = df["preco"].mean()
amostra = df.sample(frac=0.1, random_state=42)
media_amostra = amostra["preco"].mean()
print("Media População: ", round(media_populacao, 2))
print("Media Amostra: ", round(media_amostra, 2))