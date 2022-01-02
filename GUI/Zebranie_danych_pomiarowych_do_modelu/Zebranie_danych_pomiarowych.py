#Zebranie "surowych" danych pomiarowych
import matplotlib.pyplot as plt
import serial
import json
import numpy as np
from time import sleep

# Połączenie z kontrolerem
port = 'COM4'
szybkosc = 11520
hSerial = serial.Serial(port, szybkosc, timeout = 1, parity = serial.PARITY_NONE)
hSerial.reset_input_buffer()
hSerial.flush()
# Wartości początkowe
temperature_all = []
t_all = []
t_prev = 0
temperature = 0
t = 0
plik = open("Wyniki.txt", 'a')
plt.ion()
# Pobieranie i przetwarzanie danych
while True:
    tmp = hSerial.readline()
    try:
        # Format ramki JSON:
        # {"Temp":wartosc,"t":wartosc,"Temp_set":wartosc,"Kp":wartosc,"Ti":wartosc,"Td":wartosc}
        sample = json.loads(tmp)
        temperature = sample["Temp"] #Odczytanie temperatury
        temperature_all.append(temperature) #Dodanie do całego zbioru
        t = sample["t"] #Odczytanie temperatury
        t_prev = t_prev + t
        t_all.append(t) #Dodanie do całego zbioru
    except ValueError:
        print("JSON Problem")
        hSerial.flush()
        hSerial.reset_input_buffer()
    print("Temperatura: " + str(temperature) + "Czas: " + str(t_prev))
    plik.write(str(t_prev) + " " + str(temperature) + "\n") # Zapis jako plik txt w formacie CSV
    plt.plot(t_prev,temperature)
    plt.title("URA - temperatura")
    plt.xlabel("Czas t [s]")
    plt.ylabel("Temperatura [C]")
    plt.show()
    plt.pause(0.0001)
# hSerial.close()
# plik.close()