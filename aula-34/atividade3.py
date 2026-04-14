import pandas as pd

df = pd.read_csv("aula-34/vinhos.csv")

df2 = df.copy()
df2.loc[1:5, "valor_usd"] = None
df2.loc[10:15, "pais"] = None
df2.loc[3:8, "preco"] = None
df2.loc[12:18, "avaliacao"] = None

print(df2.head(20))

print(df2.isnull())
print(df2.isnull().sum())

#Exercicio 4

print(df2.describe().T)
print("-"*100)
print(df.describe().T)