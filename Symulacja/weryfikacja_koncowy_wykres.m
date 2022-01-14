%
% @Autorzy: Agnieszka Piórkowska, Mi³osz Gajewski
% @MatLab version: R2016b
% @Data: 14.01.2022
%
wyniki = importdata('WynikiPID.txt'); %plik z koñcowymi zebranymi pomiarami
Wyniki = WynikiPID;
czas = Wyniki(:,1);
temperatura = Wyniki(:,2);
liczba_probek = length(temperatura);
zadana = 27; %Do ustawienia z pomiarów

figure(1);
plot(czas,temperatura, 'b.');
hold on;
line([0 czas(end)],[zadana, zadana],'Color','red','LineStyle','--');
hold off;
title('Dane regulatora:, Kp=0.52, Ki=0.003, Kd=0.257');
xlabel('Czas (s)');
ylabel('Temperatura (C)');
legend('Zmierzone próbki');
axis tight;