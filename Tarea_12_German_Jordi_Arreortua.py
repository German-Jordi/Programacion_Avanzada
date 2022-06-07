# Tarea 12.
# Extender el programa happiness.py para que incluya lo siguiente:
# 1. La descarga de datos del índice de felicidad debe
# enviarse a un archivo csv.
# 2. El programa debe contener una función para seleccionar los
# valores de felicidad en fechas determinadas.
# Las fechas deben poderse especificar en una forma similar a los "Index slices".
# German Jordi Arreortua Reyes
# 07/06/2022
# ! ./venv/bin/python3.8
# -*- coding: utf-8 -*-
"""
Download world happiness time series from hedonometer project.
See https://hedonometer.org/timeseries/en_all/?from=2020-08-24&to=2022-02-23
Created on Tue Feb 24 15:35:23 2022

@author: Feliú Sagols
CDMX
"""

import csv
import datetime
# import pandas as pd
import requests
# import psycopg2

import loggers

TIMESERIES_DATABASE = "ts_db"

global LOGGER


# def last_available_date():
#     """
#     Returns the newest record base_date in happiness table
#     """
#     conn = psycopg2.connect("dbname=%s user=fsagols host=localhost" %
#                             TIMESERIES_DATABASE)
#     cur = conn.cursor()
#     cur.execute("""
#         select date_
#         from happiness
#         order by date_ desc
#         limit 1;
#         """)
#     date_ = cur.fetchone()[0]
#     conn.close()
#     return date_


# def get_happiness_ts(last_date, last_days):
#     """
#     Returns the happiness time series.
#
#     Parameters
#     ----------
#     last_date : datetime.pyi
#         Last base_date in the time period to download.
#     last_days:
#         Number of days previous to the last base_date to download.
#
#     Examples
#     --------
#     >>> get_happiness_ts(datetime.datetime(2022, 2, 26), 700)
#
#     Returns
#     -------
#         A dataframe with the time series.
#     """
#     conn = psycopg2.connect("dbname=%s user=fsagols host=localhost" %
#                             TIMESERIES_DATABASE)
#     cur = conn.cursor()
#     cur.execute(
#         """
#         select date_, happiness
#         from happiness
#         where date_ <= %(last_date)s
#         order by date_ desc limit %(last_days)s;
#         """, {
#             'last_date': last_date,
#             'last_days': last_days
#         })
#     answer = cur.fetchall()
#     answer.reverse()
#     answer = [[a[0], a[1]] for a in answer]
#     df = pd.DataFrame(data=answer, columns=['base_date', 'happiness'])
#     df.set_index('base_date', inplace=True)
#     return df

def download_happiness(start_date, records):
    """
    Download happiness records from the url below. Happiness records are stored
    into happiness database table.

    Parameters
    ----------
    start_date : datetime.pyi
        Initial downloading base_date.
    records : int
        Maximum number of records after start_date to download.
    """

    LOGGER.debug("Downloading happiness time series.")
    data_json = requests.get(
        'https://hedonometer.org/api/v1/happiness/?format=json&timeseries__'
        f'title=en_all&date__gte='
        f'{start_date.strftime("%Y-%m-%d")}&limit={records}')
    data = data_json.json()
    data = [[
        datetime.datetime.strptime(d['date'], "%Y-%m-%d"), d['frequency'],
        float(d['happiness'])
    ] for d in data['objects']]
    # conn = psycopg2.connect("dbname=%s user=fsagols host=localhost" %
    #                         TIMESERIES_DATABASE)
    LOGGER.info("Storing happiness time series.")
    # cur = conn.cursor()
    # cur.executemany(
    #     """
    #     insert into happiness
    #     values (%s, %s, %s)
    #     on conflict (date_)
    #     do nothing;
    #     """, data)
    # conn.commit()
    # conn.close()
    data = sorted(data, key=lambda a: a[0])

    with open("data.csv", "w", newline="") as archivo:
        archivo_writer = csv.writer(archivo, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
        archivo_writer.writerow(['date', 'frequency', 'happiness'])
        for elemento in data:
            archivo_writer.writerow(elemento)
        archivo.close()


def retrieve_happiness(intervalo_fechas):
    """
    Selecciona los valores de felicidad en fechas determinadas
    :param intervalo_fechas: lista en forma similar a los "Index slices".
    """
    for intervalo in intervalo_fechas:
        fecha_ini = datetime.datetime.strptime(intervalo[0], "%Y-%m-%d")

        if len(intervalo) > 1:
            fecha_ter = datetime.datetime.strptime(intervalo[1], "%Y-%m-%d")
        else:
            fecha_ter = fecha_ini

        if len(intervalo) > 2:
            salto = intervalo[2]
        else:
            salto = 1

        contador = salto
        with open("data.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            print(f'\t Intervalo de fechas:  {intervalo}.')
            for row in csv_reader:
                if fecha_ini <= \
                        datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S') <= \
                        fecha_ter:
                    if contador == salto:
                        print(f'\t date: {row["date"]}, frequency: {row["frequency"]},'
                              f'  happiness: {row["happiness"]}')
                        contador = 0
                    contador += 1


if __name__ == "__main__":
    LOGGER = loggers.define_logger("happiness.log")
    date = datetime.datetime(2022, 1, 1)
    download_happiness(date, 5000)

retrieve_happiness([['2022-01-01', '2022-05-24', 3], ['2022-02-01', '2022-02-07']])
# retrieve_happiness([['2022-01-01', '2022-03-27', 6],
#                    ['2022-02-01', '2022-02-07', 2], ['2022-04-01']])
