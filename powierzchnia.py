import pandas as pd

#name = input("podaj nazwę pliku(example.csv): ")

lista = pd.read_csv('lista.csv', sep=';', usecols=[0,1])
#lista = lista.to_numpy()
print(lista)

data = pd.read_csv('OrderList_1_1515.csv', engine='python', sep=';', skiprows=2, usecols=[2, 6,5, 10, 12])
data = data.dropna(subset=['Interior Finition', 'Exterior finition'], thresh = 1)
data = data.reset_index(drop=True)
data = data.drop(columns=['Interior Finition', 'Exterior finition'])
#data = data.to_numpy()


print(data)
