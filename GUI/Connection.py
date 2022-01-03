# Część odpowiadająca za połączenie programu z mikrokontrolerem i odbiór danych
from time import sleep
import serial
import json
import matplotlib as plt

port = 'COM4'
szybkosc = 11520
def Connect_to_MCU():
    hSerial = serial.Serial(port, szybkosc, timeout = 1, parity = serial.PARITY_NONE)
    hSerial.reset_input_buffer()
    hSerial.flush()
# hSerial.close() !