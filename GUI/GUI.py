###
#       Interfejs graficzny użytkownika
# @Autorzy:     Agnieszka Piórkowska i Miłosz Gajewski
# @Data:        17.01.2022
# @Uczelnia:    Politechnika Poznańska
# @Przedmiot:   Systemy mikroprocesorowe
# @Licencja:    MIT 
###
import threading
from time import sleep
import serial
import json
import matplotlib.pyplot as plt
import keyboard
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Polacz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Polacz.setGeometry(QtCore.QRect(40, 40, 80, 25))
        self.pushButton_Polacz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Polacz.setAccessibleDescription("")
        self.pushButton_Polacz.setObjectName("pushButton_Polacz")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_Status = QtWidgets.QLabel(self.centralwidget)
        self.label_Status.setGeometry(QtCore.QRect(150, 40, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Status.setFont(font)
        self.label_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Status.setObjectName("label_Status")
        self.pushButton_Rozpocznij = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Rozpocznij.setGeometry(QtCore.QRect(40, 80, 80, 25))
        self.pushButton_Rozpocznij.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Rozpocznij.setObjectName("pushButton_Rozpocznij")
        self.pushButton_temp_set = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_temp_set.setGeometry(QtCore.QRect(40, 120, 81, 51))
        self.pushButton_temp_set.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_temp_set.setObjectName("pushButton_temp_set")
        self.comboBox_temperatura = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_temperatura.setGeometry(QtCore.QRect(170, 130, 111, 25))
        self.comboBox_temperatura.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_temperatura.setEditable(False)
        self.comboBox_temperatura.setObjectName("comboBox_temperatura")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.label_Regulator = QtWidgets.QLabel(self.centralwidget)
        self.label_Regulator.setGeometry(QtCore.QRect(10, 180, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Regulator.setFont(font)
        self.label_Regulator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Regulator.setObjectName("label_Regulator")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_kp = QtWidgets.QLabel(self.centralwidget)
        self.label_kp.setGeometry(QtCore.QRect(70, 210, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_kp.setFont(font)
        self.label_kp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kp.setObjectName("label_kp")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 180, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_kd = QtWidgets.QLabel(self.centralwidget)
        self.label_kd.setGeometry(QtCore.QRect(70, 240, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_kd.setFont(font)
        self.label_kd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kd.setObjectName("label_kd")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_ki = QtWidgets.QLabel(self.centralwidget)
        self.label_ki.setGeometry(QtCore.QRect(70, 270, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_ki.setFont(font)
        self.label_ki.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ki.setObjectName("label_ki")
        self.label_temp_aktualna = QtWidgets.QLabel(self.centralwidget)
        self.label_temp_aktualna.setGeometry(QtCore.QRect(240, 250, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp_aktualna.setFont(font)
        self.label_temp_aktualna.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp_aktualna.setObjectName("label_temp_aktualna")
        self.pushButton_zapisz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zapisz.setGeometry(QtCore.QRect(230, 280, 80, 25))
        self.pushButton_zapisz.setObjectName("pushButton_zapisz")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 
        # Akcje przycisków
        # 
        # Przycisk Połącz:
        self.pushButton_Polacz.clicked.connect(self.Connect_to_MCU)
        # Przycisk Rozpocznij:
        self.pushButton_Rozpocznij.clicked.connect(self.Rozpocznij_to_MCU)
        # Przycisk Temperatura zadana
        self.pushButton_temp_set.clicked.connect(self.Temp_set_to_MCU)
        # Przycisk Zapisz
        self.pushButton_zapisz.clicked.connect(self.Zapisz_do_pliku)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "URA"))
        self.pushButton_Polacz.setText(_translate("MainWindow", "Połącz"))
        self.label.setText(_translate("MainWindow", "URA - SM"))
        self.label_Status.setText(_translate("MainWindow", "Status: Rozłączono"))
        self.pushButton_Rozpocznij.setText(_translate("MainWindow", "Rozpocznij"))
        self.pushButton_temp_set.setText(_translate("MainWindow", "Temperatura \n"
"zadana"))
        self.comboBox_temperatura.setItemText(0, _translate("MainWindow", "24°C"))
        self.comboBox_temperatura.setItemText(1, _translate("MainWindow", "25°C"))
        self.comboBox_temperatura.setItemText(2, _translate("MainWindow", "26°C"))
        self.comboBox_temperatura.setItemText(3, _translate("MainWindow", "27°C"))
        self.comboBox_temperatura.setItemText(4, _translate("MainWindow", "28°C"))
        self.comboBox_temperatura.setItemText(5, _translate("MainWindow", "29°C"))
        self.comboBox_temperatura.setItemText(6, _translate("MainWindow", "30°C"))
        self.comboBox_temperatura.setItemText(7, _translate("MainWindow", "31°C"))
        self.comboBox_temperatura.setItemText(8, _translate("MainWindow", "32°C"))
        self.comboBox_temperatura.setItemText(9, _translate("MainWindow", "33°C"))
        self.comboBox_temperatura.setItemText(10, _translate("MainWindow", "34°C"))
        self.comboBox_temperatura.setItemText(11, _translate("MainWindow", "35°C"))
        self.comboBox_temperatura.setItemText(12, _translate("MainWindow", "37°C"))
        self.comboBox_temperatura.setItemText(13, _translate("MainWindow", "38°C"))
        self.comboBox_temperatura.setItemText(14, _translate("MainWindow", "39°C"))
        self.label_Regulator.setText(_translate("MainWindow", "Regulator"))
        self.label_2.setText(_translate("MainWindow", "Kp :"))
        self.label_kp.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Temperatura</p><p>aktualna:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Kd :"))
        self.label_kd.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Ki :"))
        self.label_ki.setText(_translate("MainWindow", "0"))
        self.label_temp_aktualna.setText(_translate("MainWindow", "0"))
        self.pushButton_zapisz.setText(_translate("MainWindow", "Zapisz"))
        # 
        # Funkcje do przycisków
        #  
    def Connect_to_MCU(self):
        port = 'COM3'
        szybkosc = 115200
        self.hSerial = serial.Serial(port, szybkosc, timeout = 1, parity = serial.PARITY_NONE, bytesize = serial.EIGHTBITS) # Otworzenie portu
        self.hSerial.reset_input_buffer()
        self.hSerial.flush()
        self.label_Status.setText("Status: Połączono")
        self.label_Status.adjustSize()

    def Rozpocznij_to_MCU(self):
        self.hSerial.write(b'STA=0001') # Rozpoczęcie pracy mikrokontrolera
        # Rozpoczęcie wyświetlania wyników
        # Wartości początkowe
        # "Temp":wartosc
        self.temperature = 0 # Aktualna temperatura
        self.temperature_all = [] # Wektor temperatur
        # "t":wartosc
        self.t_all = [] # Wektor czasu
        self.t = 0 # Czas
        self.t_prev = 0 # Czas poprzedni
        # "Temp_set":wartosc
        self.temperature_set_all = [] # Wektor zadanych temperatur
        self.temperature_set = 0 # Aktulana temperatura zadana
        # "Kp":wartosc
        self.Kp = 0
        # "Ki":wartosc
        self.Ki = 0
        # "Kd":wartosc
        self.Kd = 0
        # "u":wartosc
        self.u = 0 # Sterowanie aktualne
        self.u_all = [] # Wektor sterowania
        plt.ion()
        while True:
            tmp = self.hSerial.readline()
            try:
                # Format ramki JSON:
                # {"Temp":wartosc,"t":wartosc,"Temp_set":wartosc,"Kp":wartosc,"Ki":wartosc,"Kd":wartosc,"u":wartosc}
                sample = json.loads(tmp)
                # "Temp":wartosc
                self.temperature = sample["Temp"] # Odczytanie temperatury aktualnej
                self.temperature_all.append(self.temperature) # Dodanie do całego zbioru
                # "t":wartosc
                self.t = sample["t"] # Czas
                self.t_prev = self.t_prev + self.t
                self.t_all.append(self.t_prev)
                # "Temp_set":wartosc 
                self.temperature_set = sample["Temp_set"] # Temperatura zadana
                self.temperature_set_all.append(self.temperature_set)
                # "Kp":wartosc
                self.Kp = sample["Kp"]
                self.label_kp.setText(str(self.Kp))
                self.label_kp.adjustSize()
                # "Ki":wartosc
                self.Ki = sample["Ki"]
                self.label_ki.setText(str(self.Ki))
                self.label_ki.adjustSize()
                # "Kd":wartosc
                self.Kd = sample["Kd"]
                self.label_kd.setText(str(self.Kd))
                self.label_kd.adjustSize()
                # "u":wartosc
                self.u = sample["u"] # Sygnał sterujący
                self.u_all.append(self.u)
            except ValueError:
                print("JSON Problem")
                self.hSerial.flush()
                self.hSerial.reset_input_buffer()
            self.label_temp_aktualna.setText(str(self.temperature))
            self.label_temp_aktualna.adjustSize()
            plt.clf()
            plt.plot(self.t_all,self.temperature_all,'b')
            plt.plot(self.t_all,self.temperature_set_all,'r')
            plt.legend(["Temperatura aktualna","Temperatura zadana"])
            temp_set_tunel = [i * 1.01 for i in self.temperature_set_all]
            plt.plot(self.t_all,temp_set_tunel,'g') # 1% tunel
            temp_set_tunel = [i * 0.99 for i in self.temperature_set_all]
            plt.plot(self.t_all,temp_set_tunel,'g') # 1% tunel
            temp_set_tunel = [i * 1.05 for i in self.temperature_set_all]
            plt.plot(self.t_all,temp_set_tunel,'y') # 5% tunel
            temp_set_tunel = [i * 0.95 for i in self.temperature_set_all]
            plt.plot(self.t_all,temp_set_tunel,'y') # 5% tunel
            plt.title("URA - temperatura")
            plt.xlabel("Czas t [s]")
            plt.ylabel("Temperatura [C]")
            plt.show()
            plt.pause(0.01)
            if keyboard.is_pressed("q"):
                break
    
    def Temp_set_to_MCU(self):
        wybrana_temp = self.comboBox_temperatura.currentText()
        tmp_wybrana_temp = wybrana_temp[0:2]
        self.message = "TMP="+tmp_wybrana_temp+".0"
        self.hSerial.write(bytes(self.message,'UTF-8'))

    def Zapisz_do_pliku(self):
        self.plik = open("Wyniki_URA_GUI.txt", 'a')
        for i in range(len(self.t_all)):
            self.plik.write(str(self.t_all[i]) + " " + str(self.temperature_all[i])+ " " + str(self.u_all[i]) +"\n") # Zapis jako plik txt w formacie CSV
        self.plik.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())