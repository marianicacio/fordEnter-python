import pandas as pd

df = pd.read_csv("aula-34/vinhos.csv")

print(df.head(5))
print("-"*30)
print(df)
print("-"*30)
print(df.shape)
print("-"*30)
print(df.dtypes)
print("-"*30)
print(df.describe())
