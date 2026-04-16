import pandas as pd

#Exercicio 1

df = pd.read_excel("aula-36/vinhos_tratamento.xlsx")
df2 = df.copy()
df2 = pd.concat([df, df])

print(df2.shape)
print(df2.describe())

#Exercicio 2

df3 = pd.concat([df, df])
print(df3.isnull().head())
print(df3.isnull().sum())
print(df3.isnull().sum().sum())

print(df3.shape)
print(df3.describe())

df4 = df3.drop_duplicates()
print(df4.head())
print(df4.shape)
print(df4.describe())

df5 = df3.dropna()
print(df5.head())
print(df5.shape)
print(df5.describe())

#Exercicio 3

dfFinal = df3.drop_duplicates()
print(df3.shape)
print("-"*50)
print(dfFinal.shape)

mediana_value = dfFinal["value_usd"].median()
dfFinal = df3.fillna(mediana_value)
mediana_volume = dfFinal["volume_hl"].median()
dfFinal = df3.fillna(mediana_volume)

print(dfFinal.head())

#Exercicio 4

print("\nDF ORIGINAL")
print("Shape:", df.shape)
print(df.describe().T)

print("\n" + "="*60)


print("\nDF3 (COM DUPLICATAS)")
print("Shape:", df3.shape)
print(df3.describe().T)

print("\n" + "="*60)


print("\nDFFINAL (SEM DUPLICATAS E SEM NULOS)")
print("Shape:", dfFinal.shape)
print(dfFinal.describe().T)

print("\n" + "="*60)
