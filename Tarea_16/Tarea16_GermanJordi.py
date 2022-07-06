# Tarea 16
# Germán Jordi Arreortua Reyes

"""frende de pareto"""

import csv
import timeit
import pandas as pd


def frente_de_pareto(datos):
    """
    Encuentra el frente de Pareto de una lista de
    puntos en R^n
    :param datos: arreglo
    :return: Un arreglo con los elementos
    del frente de Pareto
    """
    indices_a_comparar = []
    for ind in range(len(datos[0])):
        if not isinstance(datos[0][ind], str):
            indices_a_comparar.append(ind)

    i = 0
    while i < len(datos):
        j = i + 1
        while j < len(datos):
            if all(datos[i][k] <= datos[j][k] for k in indices_a_comparar):
                datos.pop(i)
                j = i + 1
            else:
                if all(datos[j][k] <= datos[i][k] for k in indices_a_comparar):
                    datos.pop(j)
                else:
                    j += 1
        i += 1
    return datos


# Se debe tomar en cuenta que se agregó PRICE a la última
# columna de statistics.csv
df = pd.read_csv('statistics.csv')
costos = [list(x) for x in df.values]
print(timeit.timeit('frente_de_pareto(costos)', number=100, globals=globals()))

with open('frente_de_pareto.csv', 'w', newline='') as csv_file:
    cvs_writer = csv.writer(csv_file)
    cvs_writer.writerow(['Symbol 1', 'Symbol 2', 'APR', 'SHARPE',	'PRICE'])
    for dato in frente_de_pareto(costos):
        cvs_writer.writerow(dato)
