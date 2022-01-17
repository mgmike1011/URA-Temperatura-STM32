#Zebranie "surowych" danych pomiarowych
import matplotlib.pyplot as plt
import serial
import json
import numpy as np
from time import sleep
import keyboard

# Połączenie z kontrolerem
port = 'COM3'
szybkosc = 115200
hSerial = serial.Serial(port, szybkosc, timeout = 1, parity = serial.PARITY_NONE, bytesize = serial.EIGHTBITS)
hSerial.reset_input_buffer()
hSerial.flush()
# Wartości początkowe
temperature_all = []
t_all = []
t_prev = 0
u_all = []
u = 0
temperature = 0
t = 0
temperature_set = 0
temperature_set_all = []
plik = open("Wyniki_PID.txt", 'a')
plt.ion()
hSerial.write(b'TMP=27.0') # Ustawienie zadanej temperatury
hSerial.write(b'STA=0001') # Rozpoczęcie pracy mikrokontrolera
# Pobieranie i przetwarzanie danych
while True:
    tmp = hSerial.readline()
    try:
        # Format ramki JSON:
        # {"Temp":wartosc,"t":wartosc,"Temp_set":wartosc,"Kp":wartosc,"Ki":wartosc,"Kd":wartosc,"u":wartosc}
        sample = json.loads(tmp)
        temperature = sample["Temp"] # Odczytanie temperatury aktualnej
        temperature_all.append(temperature) # Dodanie do całego zbioru
        t = sample["t"] # Czas
        t_prev = t_prev + t
        t_all.append(t_prev) 
        u = sample["u"] # Sygnał sterujący
        u_all.append(u)
        temperature_set = sample["Temp_set"] # Temperatura zadana
        temperature_set_all.append(temperature_set)
    except ValueError:
        print("JSON Problem")
        hSerial.flush()
        hSerial.reset_input_buffer()
    plik = open("Wyniki_PID.txt", 'a')
    print("Temperatura: " + str(temperature) + " Czas: " + str(t_prev)+ " Sterowanie: " + str(u))
    plik.write(str(t_prev) + " " + str(temperature) + str(u) +"\n") # Zapis jako plik txt w formacie CSV
    plik.close()
    plt.clf()
    plt.plot(t_all,temperature_all,'b')
    plt.plot(t_all,temperature_set_all,'r')
    plt.legend(["Temperatura aktualna","Temperatura zadana"])
    plt.plot(t_all,temperature_set_all*1.01,'g') # 1% tunel
    plt.plot(t_all,temperature_set_all*0.99,'g') # 1% tunel
    plt.plot(t_all,temperature_set_all*1.05,'y') # 5% tunel
    plt.plot(t_all,temperature_set_all*0.95,'y') # 5% tunel
    plt.title("URA - temperatura")
    plt.xlabel("Czas t [s]")
    plt.ylabel("Temperatura [C]")
    plt.show()
    plt.pause(0.01)
    if keyboard.is_pressed("q"):
        break
hSerial.close()