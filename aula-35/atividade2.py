#Exercicio 2

import pandas as pd

data_frame = pd.read_excel("aula-35/vinhos_exercicio.xlsx")

print(data_frame.sort_values(by=["year"], ascending= [False])) 
print(data_frame.sort_values(by=["value_usd"], ascending= [False])) 

print(data_frame.iloc[:, [0, 1, 4, 5, 6]])

#Exercicio 3

print(data_frame.loc[:9, 'year'])
