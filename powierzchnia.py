import pandas as pd
import numpy as np
suma = 0
np.set_printoptions(suppress=True)

plik = input("podaj nazwę pliku(example.csv): ")

lista = pd.read_csv('lista.csv', sep=';', usecols=[0,1])
lista = lista.astype(str)


data = pd.read_csv(plik, engine='python', sep=';', skiprows=2, usecols=[2, 6,5, 10, 12])
data = data.dropna(subset=['Interior Finition', 'Exterior finition'], thresh = 1)
data = data.reset_index(drop=True)
data = data.drop(columns=['Interior Finition', 'Exterior finition'])
data = data.astype(str)
#data = data.to_numpy()

result = pd.merge(lista, data, how='left', on=['Order reference'])
result = result.dropna()
result = result.reset_index(drop=True)
result = result.to_numpy()

for i in range (0, len(result)):
    pow = float(result[i,1])*float(result[i,2])*float(result[i,3])
    pow = pow/1000
    suma = suma + pow
    
pow_lak = suma / 100

print(f'Powierzchnia lakierowana wynosi: {pow_lak} m2')

