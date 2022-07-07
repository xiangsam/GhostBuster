clear
%close all

%% 参数设置
Fs = 4e6;


data = read_complex_binary('test_gain/QCA6174');
% dataC = read_complex_binary('test_gain/afterChannelAC');

% 9000(packet_nums) * 80
% datasize = 0.1 * 2e6;
% datasize = 12000 * 80;
% data = data(1:datasize);
% data = data(1:datasize);

%% FFT
fest2_temp = Fs/length(data);
fest2 = -Fs/2 : fest2_temp : Fs/2-fest2_temp;
figure;
plot(fest2, fftshift(abs(fft(data))));
title FFT

% fest2_temp = Fs/length(dataB);
% fest2 = -Fs/2 : fest2_temp : Fs/2-fest2_temp;
% figure;
% plot(fest2, fftshift(abs(fft(dataB))));
% title MIMOB
% 
%
%%信噪比计算
tmp = abs(fft(data));
signalpower = max(tmp.^2);
noisepower = mean(tmp(100: 5000).^2);
snrA = 10*log10(signalpower / noisepower);
% 
% 
% tmp = abs(fft(dataB));
% signalpower = max(tmp.^2);
% noisepower = mean(tmp(10000: 50000).^2);
% snrB = 10*log10(signalpower / noisepower);

