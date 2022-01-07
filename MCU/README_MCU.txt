##########
#
#	@Data:		01.01.2022
#	@Autorzy:	Agnieszka Piórkowska, Miłosz Gajewski
#	@Projekt:	SM_lab_projekt_URA
#	@Part:		Program sterujący mikrokontrolerem (MCU)
#
##########
-- MCU --

Program realizuje sterowanie mikrokontrolerem: wysyłanie i odbiór danych, realizacja algorytmu sterowania URA, wyświetlanie wyników.

#Elementy fizyczne:
- Rezystor 39Ohm,
- Tranzystor bipolarny NPN,
- Czujnik BMP280,
- Wyświetlacz OLED, ze sterownikiem SSD1306,
- Przewody połączeniowe,
- Zasilacz zewnętrzny 5V i 3.3V, 

#Wyświetlacz OLED, ze sterownikiem SSD1306:
Połączenie: I2C

#Czujnik BMP280:
Połączenie: SPI

#Wysyłanie i odbiór danych:
Połączenie: UART 3,
Format ramki JSON przy wysyłaniu: {\"Temp\":%.2f,\"t\":%.1f,\"Temp_set\":%.2f,\"Kp\":%.4f,\"Ki\":%.4f,\"Kd\":%.4f,\"u\":%.2f}\r\n
Obsługiwane komendy odbioru: "TMP=**.*" - ustwienie zadanej temperatury, "STA=****" - zmiana stanu pracy układu

#Liczniki:
TIM3 - generowanie sygnału PWM (Channel_3)
TIM2 - próbkowanie

#Sygnalizacja spracy:
LD1 -	dioda zielona 		-	odbiór danych przez UART
LD2	-	dioda niebieska 	-	działanie algorytmu regulatora

-- Wykorzystane biblioteki i zasoby --
#Implementacja algorytmu regulatora:
/*
 * PID_Controller.h
 *
 *  Created on: 3 sty 2022
 *      Author: Agnieszka Piórkowska i Miłosz Gajewski
 */
Stworzone na bazie materiałów do przedmiotu Systemy mikroprocesorowe - Politechnika Poznańska 2021.

#Czujnik BMP280:
/*
 * BMPXX0.h
 *
 *  The MIT License.
 *  Based on Adafuit libraries.
 *  Created on: 10.08.2018
 *      Author: Mateusz Salamon
 *      www.msalamon.pl
 *
 */
 
#Wyświetlacz OLED z kontrolerem SSD1306:
/*
 * SSD1306_OLED.h
 *
 *  Created on: Oct 29, 2020
 *      Author: Mateusz Salamon
 *      www.msalamon.pl
 */
Licencja: MIT
 
#Biblioteka graficzna do wyświetlacza:
/*
 * GFX_BW.h
 *
 *  The MIT License.
 *  Created on: 25.05.2017
 *      Author: Mateusz Salamon
 *      www.msalamon.pl
 *      mateusz@msalamon.pl
 */
 
#Czcionki do wyświetlacza:
/*
 * fonts.h
 *
 *  The MIT License.
 *  Created on: 25.05.2017
 *      Author: Mateusz Salamon
 *      www.msalamon.pl
 *      mateusz@msalamon.pl
 */
