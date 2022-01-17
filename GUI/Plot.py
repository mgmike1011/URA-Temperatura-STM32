# Część odpowiedzialna za przedstawienie wyników
from Connection import *
import matplotlib.pyplot as plt
import json
import numpy as np
from time import sleep


def Plot_Init():
    # Wartości początkowe
    # "Temp":wartosc
    temperature = 0 # Aktualna temperatura
    temperature_all = [] # Wektor temperatur
    # "t":wartosc
    t_all = [] # Wektor czasu
    t = 0 # Czas
    t_prev = 0 # Czas poprzedni
    # "Temp_set":wartosc
    temperature_set_all = [] # Wektor zadanych temperatur
    temperature_set = 0 # Aktulana temperatura zadana
    # "Kp":wartosc
    Kp = 0
    # "Ki":wartosc
    Ki = 0
    # "Kd":wartosc
    Kd = 0
    # "u":wartosc
    u = 0 # Sterowanie aktualne
    u_all = [] # Wektor sterowania
    plt.ion()
    Connect_to_MCU()



def get_data():
    tmp = hSerial.readline()
    try:
        # Format ramki JSON:
        # {"Temp":wartosc,"t":wartosc,"Temp_set":wartosc,"Kp":wartosc,"Ki":wartosc,"Kd":wartosc,"u":wartosc}
        sample = json.loads(tmp)
        # "Temp":wartosc
        temperature = sample["Temp"] # Odczytanie temperatury aktualnej
        temperature_all.append(temperature) # Dodanie do całego zbioru
        # "t":wartosc
        t = sample["t"] # Czas
        t_prev = t_prev + t
        t_all.append(t_prev)
        # "Temp_set":wartosc 
        temperature_set = sample["Temp_set"] # Temperatura zadana
        temperature_set_all.append(temperature_set)
        # "Kp":wartosc
        Kp = sample["Kp"]
        # "Ki":wartosc
        Ki = sample["Ki"]
        # "Kd":wartosc
        Kd = sample["Kd"]
        # "u":wartosc
        u = sample["u"] # Sygnał sterujący
        u_all.append(u)
    except ValueError:
        print("JSON Problem")
        hSerial.flush()
        hSerial.reset_input_buffer()

def show_plot():
    get_data()
    plt.title("URA - Przebieg temperatury")
    plt.xlabel("Czas t [s]")
    plt.ylabel("Temperatura [C]")
    plt.plot(t,temperature)
    plt.show()
    plt.pause(0.01)