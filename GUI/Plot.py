# Część odpowiedzialna za przedstawienie wyników
from Connection import *
import matplotlib.pyplot as plt
import json
import numpy as np
from time import sleep


def Plot_Init():
    plt.ion()
    Connect_to_MCU()

temperature_all = []
t_all = []
temperature = 0
t = 0

def get_data():
    tmp = hSerial.readline()
    try:
        sample = json.loads(tmp)
        temperature = sample["Temp"] #Odczytanie temperatury
        temperature_all.append(temperature) #Dodanie do całego zbioru
        t = sample["t"] #Odczytanie temperatury
        t_all.append(t) #Dodanie do całego zbioru
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
    plt.pause(0.0001)