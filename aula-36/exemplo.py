import pandas as pd

df = pd.read_excel("aula-36/vinhos_tratamento.xlsx")
df2 = df.copy()
df2.loc[1:1, "value_usd"]=None
df3 = df2.copy()
print(df3.head())
media_value = df3["value_usd"].mean()
df3 = df3.fillna(media_value)
print("-"*50)
print(df3.head())