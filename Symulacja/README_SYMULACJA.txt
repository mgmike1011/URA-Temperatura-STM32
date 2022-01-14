##########
#
#	@Data:		01.01.2022
#	@Autorzy:	Agnieszka Piórkowska, Miłosz Gajewski
#	@Projekt:	SM_lab_projekt_URA
#	@Part:		Symulacja układu automatycznej regulacji (URA)
#
##########
-- URA --

W przygotowaniu plików symulacyjnych, strojeniu regulatora oraz weryfikacji danych użyto pakietu MatLab R2016b z licencją STUDENT.

Do strojenia regulatora (doboru nastaw) użyto dodatku PIDTuner.

Nastawy regualtora PID:
Kp = 0.52
Ki = 0.003
Kd = 0.257

Pliki:
# okreslenie_modelu_obiektu.m:
%
% @Autorzy: Agnieszka Piórkowska, Miłosz Gajewski
% @MatLab version: R2016b
% @Data: 14.01.2022
%
Przygotowane na podstawie materiałów wykładowych Systemy mikroprocesorowe - Politechnika Poznańska 2021/2022.
Licencja: MIT

#weryfikacja_koncowy_wykres.m
%
% @Autorzy: Agnieszka Piórkowska, Miłosz Gajewski
% @MatLab version: R2016b
% @Data: 14.01.2022
%
Przygotowane na podstawie materiałów wykładowych Systemy mikroprocesorowe - Politechnika Poznańska 2021/2022.
Licencja: MIT

#Symulacja_z_regulatorem_Simulink.mdl
%
% @Autorzy: Agnieszka Piórkowska, Miłosz Gajewski
% @MatLab version: R2016b
% @Data: 14.01.2022
%
Przygotowane na podstawie materiałów wykładowych Systemy mikroprocesorowe - Politechnika Poznańska 2021/2022.
Licencja: MIT