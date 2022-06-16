# Tarea 13.
# Entrega: Jueves 16 de junio
# Germán Jordi Arreortúa Reyes

# Escriba un programa que descargue de alguna fuente como yahoo-finance, bloomberg,
# investing, etc, la cotización del peso-dólar (usd/mxn). El programa debe
# ejecutarse de manera permanente y exactamente a las 7, 8, 9, ..., 15 y 16 horas
# de todos los días debe descargar la cotización y agregarla junto con la hora y
# fecha a un archivo csv.


import csv
import datetime
import requests
from time import sleep
from bs4 import BeautifulSoup


URL = "https://www.google.com/finance/quote/USD-MXN"
actual = datetime.datetime.now()
delta = 60*60 - (actual.minute*60 + actual.second)
if delta != 60*60:
    # Se espera hasta una hora exacta
    sleep(delta)

while True:
    actual = datetime.datetime.now()
    if actual.hour < 7:
        # Se espera hasta las 7
        sleep(7 * 60 * 60 - (actual.hour * 60 * 60 + actual.minute * 60 + actual.second))

    actual = datetime.datetime.now()
    while 7 <= actual.hour <= 16:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        dolar = soup.find('div', class_="YMlKec fxKbKc").text
        with open("dolar-peso.csv", "a", newline="") as archivo:
            archivo_writer = csv.writer(archivo)
            archivo_writer.writerow([dolar, actual])
            archivo.close()
        sleep(60 * 60 - (actual.minute * 60 + actual.second))
        actual = datetime.datetime.now()

    actual = datetime.datetime.now()
    if actual.hour > 16:
        # Se espera hasta las 0 horas
        sleep(24 * 60 * 60 - (actual.hour * 60 * 60 + actual.minute * 60 + actual.second))
