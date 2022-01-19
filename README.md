# Systemy mikroprocesorowe - Projekt URA

## Projekt układu regulacji automatycznej zrealizowany na przedmiot Systemy mikroprocesorowe 2021/2022

***GUI***: Graficzny interfejs użytkownika, który pozwala na komunikację z jednostką mikrokontrolera w obie strony (wysyłanie i odbiór danych), oraz graficzną wizualizacje działania układu. Program został stworzony w języku Python z wykorzystaniem trzech głównych bibliotek:
- PyQt5 – stworzenie aplikacji okienkowej,
-	Matplotlib – wizualizacja danych w czasie rzeczywistym,
-	Serial – obsługa połączenia z mikrokontrolerem.
W katalogu znajduje się również uproszczony skrypt w języku Python służący jedynie do odbierania i wizualizacji danych pomiarowych. Dane zapisywane są w pliku txt w formacie CSV(dane oddzielone spacjami).
>**Dokładne informacje znajdują się w pliku [README_GUI.txt](https://github.com/mgmike1011/SM_lab_projekt_URA/blob/main/GUI/README_GUI.txt) (folder GUI).**

***MCU***: Program sterujący pracą mikrokontrolera, realizacjy algorytm regulacji (sterownik PID) oraz obsługę komunikacji z komputerem.
Wykorzystane elementy fizyczne:
- Nucleo F746ZG
- Rezystor 39Ohm,
- Tranzystor bipolarny NPN - 2SD882Y,
- Czujnik BMP280,
- Wyświetlacz OLED, ze sterownikiem SSD1306,
- Przewody połączeniowe,
- Zasilacz zewnętrzny 5V i 3.3V,
Wykorzystane biblioteki oraz sposób implementacji znajduje się w pliku *README_MCU.txt*.
>**Dokładne informacje znajdują się w pliku [README_MCU.txt](https://github.com/mgmike1011/SM_lab_projekt_URA/blob/main/MCU/README_MCU.txt) (folder MCU).**

***Symulacja***: Część odpowiedzialna za strojenie regulatora (dobór nastaw), weryfikacje poprawności działania układu, oraz obliczenie jakości sterownia. W przygotowaniu plików symulacyjnych, strojeniu regulatora oraz weryfikacji danych użyto pakietu MatLab R2016b z licencją STUDENT.
Nastawy regualtora PID:
- Kp = 0.52
- Ki = 0.003
- Kd = 0.257
>**Dokładne informacje znajdują się w pliku [README_SYMULACJA.txt](https://github.com/mgmike1011/SM_lab_projekt_URA/blob/main/Symulacja/README_SYMULACJA.txt) (folder GUI).**

`Wszystkie informacje o licencjach użytych do przygotowania projektu bibliotek programistycznych oraz innych elementów znajdują się w plikach *README* poszczególnych części projektu.`

## Autorzy: Agnieszka Piórkowska i Miłosz Gajewski.

### Politechnika Poznańska 2022
