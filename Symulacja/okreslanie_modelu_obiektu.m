czas = Wyniki(:,1);
temperatura = Wyniki(:,2);
liczba_probek = length(temperatura);

% Sygna³ wejœciowy
amplituda_wejsciowa = 1; % Zale¿y od wype³nienia PWM, jeœli przyk³adowo
%PWM 90% (PWM1=90), to amplituda = 0.9 
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

offset = Wyniki(1,2);
 k = 16.413;
 T = 237.67;
 tau = 6.302;

% Obiekt na podstawie dopasowania:
% !!!! Odkomentuj, gdy wyeksportujesz dane z pidTuner !!!!
s = tf('s');
%  %k = Plant1.Kp; %Plant1.Kp;
%  T = Plant1.Tp1;
%  delay = Plant1.Td;
 H = k/(1+s*T)*exp(-s*tau); % model
 disp(sprintf('Parametry modelu: k=%.2g, T=%g, delay=%g\n', k, T, tau));

% OdpowiedŸ modelu:
% !!!! Odkomentuj, gdy wyeksportujesz dane z pidTuner !!!!
 odpowiedz_modelu = lsim(H,wejscie,czas);
 odpowiedz_modelu = odpowiedz_modelu + offset; % offset - wartoœæ pierwszej temperatury
 
% B³¹d modelu:
% !!!! Odkomentuj, gdy wyeksportujesz dane z pidTuner !!!!
 residuum = temperatura - odpowiedz_modelu; %gdyby plik wierszowy to 
%odpowiedz_modelu ' (tranzpozycja)
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