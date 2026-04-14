import pandas as pd

df = pd.read_csv("aula-34/vinhos.csv")

print(df.describe().T)
