#Zebranie "surowych" danych pomiarowych
import matplotlib.pyplot as plt
import serial
import json
import numpy as np
from time import sleep
import keyboard #pip install keyboard

# Połączenie z kontrolerem
port = 'COM3'
szybkosc = 115200
hSerial = serial.Serial(port, szybkosc, timeout = 1, parity = serial.PARITY_NONE, bytesize = serial.EIGHTBITS)
# hSerial.write(b'STA=0001') #Rozpoczęcie pracy mikrokontrolera
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
hSerial.write(b'STA=0001')
# Pobieranie i przetwarzanie danych
while True:
    tmp = hSerial.readline()
    # print(tmp)
    try:
        # Format ramki JSON:
        # {"Temp":wartosc,"t":wartosc,"Temp_set":wartosc,"Kp":wartosc,"Ki":wartosc,"Kd":wartosc,"u":wartosc}
        sample = json.loads(tmp)
        temperature = sample["Temp"] #Odczytanie temperatury
        temperature_all.append(temperature) #Dodanie do całego zbioru
        t = sample["t"] #Odczytanie temperatury
        t_prev = t_prev + t
        t_all.append(t_prev) #Dodanie do całego zbioru
    except ValueError:
        print("JSON Problem")
        hSerial.flush()
        hSerial.reset_input_buffer()
    plik = open("Wyniki.txt", 'a')
    print("Temperatura: " + str(temperature) + " Czas: " + str(t_prev))
    plik.write(str(t_prev) + " " + str(temperature) + "\n") # Zapis jako plik txt w formacie CSV
    plik.close()
    plt.clf()
    plt.plot(t_all,temperature_all)
    plt.title("URA - temperatura")
    plt.xlabel("Czas t [s]")
    plt.ylabel("Temperatura [C]")
    plt.show()
    plt.pause(0.01)
    if keyboard.is_pressed("q"):
        break  # finishing the loop
hSerial.close()