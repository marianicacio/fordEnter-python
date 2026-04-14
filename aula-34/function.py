import pandas as pd

df = pd.read_csv("aula-34/vinhos.csv")
# print(df.head(4)) //Primeiros itens na lista
# print(df.describe())
# df2 = list(df.columns)
# print(df2)
print(df.tail(3)) #Ultimos itens
print(df.shape) #Para saber quantas colunas e linhas
print(df.columns) #Mostra as colunos

df2 = df.copy()
df2.loc[1:10, "valor_usd"] = None
print(df2.head(10))

print(df2.isnull().sum())
