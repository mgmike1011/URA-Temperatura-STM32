wyniki = importdata('Wyniki_koncowe.txt'); %plik z koñcowymi zebranymi pomiarami
czas = Wyniki(:,1);
temperatura = Wyniki(:,2);
liczba_probek = length(temperatura);
zadana = 26; % tu ustaw nasz¹

figure(1);
plot(czas,temperatura, 'b.');
hold on;
line([0 czas(end)],[zadana, zadana],'Color','red','LineStyle','--');
hold off;
title('Dane regulatora:, Kp=wpisz, Ki=wpisz, Kd=wpisz');
xlabel('Czas (s)');
ylabel('Temperatura (C)');
legend('Zmierzone próbki');
axis tight;