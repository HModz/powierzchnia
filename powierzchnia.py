import numpy as np
import pandas as pd

suma = 0
np.set_printoptions(suppress=True)

plik = input("podaj nazwę pliku(example.csv): ")

lista = pd.read_csv('lista.csv', sep=';', usecols=[0, 1])
lista = lista.astype(str)

data = pd.read_csv(plik, engine='python', sep=';', skiprows=2, usecols=[2, 4, 6, 5, 10, 12])
data = data.dropna(subset=['Interior Finition', 'Exterior finition'], thresh=1)
data = data.reset_index(drop=True)

accessory = data.to_numpy()

data = data.drop(columns=['Interior Finition', 'Exterior finition', 'Description'])
data = data.astype(str)

result = pd.merge(lista, data, how='left', on=['Order reference'])
result = result.dropna()
result = result.reset_index(drop=True)
result = result.to_numpy()

for i in range(0, len(result)):
    powierzchnia = float(result[i, 1]) * float(result[i, 2]) * float(result[i, 3])
    powierzchnia = powierzchnia / 1000
    suma = suma + powierzchnia

pow_lak = suma / 100

print(f'Powierzchnia lakierowana wynosi: {pow_lak} m2', '\n')

print('Akcesoria:')
for i in range(0, len(accessory)):
    if accessory[i, 3] == 1:
        print(f'{accessory[i, 1]} sztuk: {accessory[i, 2]}')
