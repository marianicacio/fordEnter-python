import pandas as pd

data_frame = pd.read_excel("aula-35/vinhos_exercicio.xlsx")
print(data_frame[(data_frame["grape_type"] == "Wine") & (data_frame["location_type"] == "Brazil_State") & (data_frame["category"] == "Sales")])
# print("-"*100)
# print(data_frame[data_frame["location_type"] == "Brazil_State"])
# print("-"*100)
# print(data_frame[data_frame["category"] == "Sales"])


data_frame2 = data_frame.copy()
print(data_frame2[(data_frame2["grape_type"] == "Table") & (data_frame2["category"] == "Sales")])
# print(data_frame2[data_frame2["grape_type"] == "Table"])
# print("-"*100)
# print(data_frame2[data_frame2["category"] == "Sales"])

print(f"Descrição dataFrame 1: {data_frame.describe().T}")
print(f"Descrição dataFrame 2: {data_frame2.describe().T}")
media1 = data_frame["value_usd"].mean()
media2 = data_frame["value_usd"].mean()

if(media1 > media2):
    print(f"Primeiro data frame é maior: {media1}")
elif(media2 > media1):
    print(f"Segundo data frame é maior: {media2}")
else:
     print(f"Eles são iguais: {media1} {media2}")

#Exercicio 2

print(data_frame.sort_values(by=["year"], ascending= [False])) 
print(data_frame.sort_values(by=["value_usd"], ascending= [False])) 

print(data_frame.iloc[:, [0, 1, 4, 5, 6]])

#Exercicio 3

print(data_frame.loc[:9, 'year'])

#Exercicio 4
print(data_frame.sort_values(by=["value_usd"], ascending= [False]).head(1))
print("-"*100)
print(data_frame2.sort_values(by=["value_usd"], ascending= [False]).head(1))

print(data_frame[data_frame["category"] == "Import"].sort_values(by=["value_usd"], ascending=False).head(1))
print("-"*100)
print(data_frame2[data_frame2["category"] == "Import"].sort_values(by=["value_usd"], ascending=False).head(1))
print("-"*100)

print(data_frame2[data_frame2["category"] == "Export"].sort_values(by=["value_usd"], ascending=False).head(1))
print("-"*100)
print(data_frame[data_frame["category"] == "Export"].sort_values(by=["value_usd"], ascending=False).head(1))