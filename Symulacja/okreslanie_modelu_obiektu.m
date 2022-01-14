%
% @Autorzy: Agnieszka Piórkowska, Mi³osz Gajewski
% @MatLab version: R2016b
% @Data: 14.01.2022
%
czas = Wyniki(:,1);
temperatura = Wyniki(:,2);
liczba_probek = length(temperatura);

% Sygna³ wejœciowy
amplituda_wejsciowa = 1;
wejscie = amplituda_wejsciowa*ones( 1 ,liczba_probek);

% Aby wyznaczyæ parametry obiektu:
% 1. Wpisujemy w CommandWindow "pidTuner"
% 2. W "Type" wybieramy PID, w "Plant" opcjê "Identify New Plant"
% 3. Get I/O data -> Arbitary I/O, w output wpisujemy "temperatura", w
% input wpisujemy "wejscie"
% 4. Zaznaczamy opcjê "Delay" (bo obiekt z opóŸnieniem); Structure: One
% Pole
% 5. Preprocess -> Remove Offset -> Remove from: Output; Offset to Remove:
% Initial value
% 6. Auto estimate
% 7. Wchodzimy w PID Tuner -> Export -> Plant1 (albo wpisujemy parametry
% rêcznie do kodu k, T, delay

% Obiekt na podstawie dopasowania:
s = tf('s');
offset = Wyniki(1,2);
k = 16.413;
T = 237.67;
tau = 6.302;
H = k/(1+s*T)*exp(-s*tau); % model
disp(sprintf('Parametry modelu: k=%.2g, T=%g, delay=%g\n', k, T, tau));

% OdpowiedŸ modelu:
odpowiedz_modelu = lsim(H,wejscie,czas);
odpowiedz_modelu = odpowiedz_modelu + offset; % offset - wartoœæ pierwszej temperatury

% B³¹d modelu:
residuum = temperatura - odpowiedz_modelu;
suma_abs_bledow = sum(abs(residuum));
disp(sprintf('Suma b³êdów(abs(residuum)) = %g\n', suma_abs_bledow));

figure(1);
plot(czas,temperatura, '.', czas, odpowiedz_modelu, '.');
title('Pomiary i odpowiedŸ obiektu');
xlabel('Czas (s)');
ylabel('Temperatura (C)');
legend('zmierzone próbki', 'odpowiedŸ uk³adu heater+BMP280');
axis tight;

figure(2);
plot(czas,residuum, '.');
title('Residuum (zmierzone próbki - odpowiedŸ uk³adu)');
xlabel('Czas (s)');
ylabel('Temperatura (C)');
axis tight;
ylim([-0.5 0.5]);