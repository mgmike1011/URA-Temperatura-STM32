##########
#
#	@Data:		01.01.2022
#	@Autorzy:	Agnieszka Piórkowska, Miłosz Gajewski
#	@Projekt:	SM_lab_projekt_URA
#	@Part:		Interfejs programu (GUI)
#
##########
-- GUI --

Program służy do graficznej komunikacji z mikrokontrolerem, akwizycji zebranych pomiarów oraz przedstawiania ich na żywo w trakcie działania algorytmu sterowania.

#Obsługa:
1)Połączenie z mikrokontrolerem za pomocą przycisku "Połącz" - w przypadku poprawnego połączenia status zmieni się na "Połączony",
2)Wybranie zadanej temperatury oraz wysłanie jej do mikrokontrolera przyciskiem "Temperatura zadana",
3)Rozpoczęcie działania programu oraz pracy mikrokontrolera następuje po przyciśnięciu przycisku "Rozpocznij",
4)Opcjonalne - zapisanie uzyskanych danych do pliku .txt w formacie CSV(dane oddzielone spacjami).

#Format danych w pliku txt:
Uzyskane dane z pomiarów mogą zostać zapisane do pliku "Wyniki_URA_GUI.txt", w formacie "Czas Temperatura Sterowanie", gdzie Czas - wartość czasu jaka upłynęła od rozpoczęcia programu, Temperatura - wartość temperatury jaka została zmierzona w danym czasie, Sterowanie - wartość sygnału sterującego obliczonego przez algorytm sterownika PID w danym czasie.

#Biblioteki
Graficzny interfejs użytkownika został zamodelowany w języku Python z wykorzystaniem biblioteki PyQT5 (licencja GPL). Wyświetlanie danych na żywo odbywa się za pomocą biblioteki Matplotlib (licencja PSF).

### Pliki ###
GUI.py
###
#       Interfejs graficzny użytkownika
# @Autorzy:     Agnieszka Piórkowska i Miłosz Gajewski
# @Data:        17.01.2022
# @Uczelnia:    Politechnika Poznańska
# @Przedmiot:   Systemy mikroprocesorowe
# @Licencja:    MIT 
###