import pandas as pd

data_frame = pd.read_excel("aula-35/vinhos_exercicio.xlsx")
data_frame.sort_values(by=["year"], ascending=True, inplace=True)
data_frame.reset_index(drop=True, inplace=True)
# print(data_frame)
data_frame[data_frame["grape_type"] == "Wine"]
print(data_frame)
