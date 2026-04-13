import pandas as pd

df = pd.read_csv("aula-34/vinhos.csv")
# print(df.head(4))
# print(df.describe())
df2 = list(df.columns)
print(df2)