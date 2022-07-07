clear;
close all;

%% 参数设置
NFFT = 64; % 子载波数，每个OFDM符号含有的符号数
num_of_subcarrier = 52; % 非空子载波数
num_of_pilot_subcarrier = 4; % 导频子载波数
num_of_data_subcarrier = num_of_subcarrier - num_of_pilot_subcarrier; % 数据子载波数
ratio_CP = 1/4; % 保护间隔占OFDM symbol的比例
CP_length = ratio_CP*NFFT; % 保护间隔长度
per_OFDMsymbol_len = NFFT + CP_length; % 每个完整OFDM符号长度
index_of_pilot = [-21 -7 7 21] + NFFT/2 + 1; % 导频子载波位置
index_of_data = [-26:-22 -20:-8 -6:-1 1:6 8:20 22:26] + NFFT/2 + 1; % 数据子载波位置
M = 2; % QPSK，每个符号上的比特数

f_delta = 2e6/NFFT; % 子载波频率间隔
B = NFFT * f_delta; % 频谱宽度
Tused = 1/f_delta; % 有效数据部分符号时间
Tgi = ratio_CP * Tused; % 保护间隔时间
Tsym = Tused + Tgi; % OFDM符号时间
Tsample = Tused/NFFT; % 采样时间间隔
Fs = 1/Tsample; % 采样频率
f_std = 0 : NFFT-1; % f标准值
DC_bin = 2^6 / NFFT;



% num_of_OFDMsymbol_per_packet = 12000; % 每packet的OFDM符号数
% num_of_OFDMsymbol_per_packet = 12000;
num_of_OFDMsymbol_per_packet = 12000;
num_of_packets = 1; % packet数
datasize = num_of_packets * num_of_OFDMsymbol_per_packet * 80;
fest_temp = Fs/datasize;
fest = -Fs/2 : fest_temp : Fs/2-fest_temp;

%%数据分段
data_ini0 = read_complex_binary('0520_seperate/afterChannelAA');
abs_data_ini0 = abs(data_ini0);
figure
t = 1 : length(abs_data_ini0);
plot(abs_data_ini0);
title MIMOA接收数据时域图
seperator = find(abs_data_ini0 > (min(abs_data_ini0) + max(abs_data_ini0)) * 3 / 4, 1);
% onlyear_part = data_ini0(1:seperator - 1000);
onlyear_part = data_ini0(1 : max(seperator-1000, datasize));
ofdm_part = data_ini0(seperator-110: end);

%%计算MIMO A 窃听器本振位置以及SNR
dataA = onlyear_part(1:datasize);
figure
fftshift_abs_fft_dataA = fftshift(abs(fft(dataA)));
plot(fest, fftshift_abs_fft_dataA);
title 无信号传输\_MIMOA
tmp = abs(fft(dataA));
tmp = tmp(1:10000);
[signalpower,max_idx]= max(tmp.^2);
noisepower = mean(tmp(max_idx+2000: end).^2);
snrA = 10*log10(signalpower / noisepower);
    
%%包定位
payloadAA = read_complex_binary('0520_seperate/payload_streamAA');
mul = read_complex_binary('0520_seperate/beforeDemuxAA');
abs_mul = abs(mul);
seperator = find(abs_mul > (min(abs_mul) + max(abs_mul)) * 3 / 4, 1);
mul = mul(seperator-110:end);
mul = mul.';
ini = 0;
idx=-1;
while true
    tmp1 = payloadAA(64*ini+1:64*(ini+1));
    tmp2 = payloadAA(64*(ini+1)+1:64*(ini+2));
    tmp3 = payloadAA(64*(ini+2)+1:64*(ini+3));
    idx1 = strfind(mul(1:end), tmp1.');
    idx2 = strfind(mul(1:end), tmp2.');
    idx3 = strfind(mul(1:end), tmp3.');
    disp(idx1);
    disp(idx2);
    disp(idx3);
    if isempty(idx1) || isempty(idx2) || isempty(idx3)
        
    elseif (idx2 - idx1 == 80) && (idx3-idx2 == 80)
        idx = idx1;
        break
    end
    ini = ini + 1;
end
data_iniA = ofdm_part(idx-CP_length:idx-CP_length+per_OFDMsymbol_len*num_of_OFDMsymbol_per_packet -1);
% data_iniA = mul(idx-CP_length:idx-CP_length+per_OFDMsymbol_len*num_of_OFDMsymbol_per_packet -1);

%%数据分段
data_ini1 = read_complex_binary('0520_seperate/afterChannelAB');
abs_data_ini1 = abs(data_ini1);
figure
plot(abs_data_ini1);
title MIMOB接收数据时域图
seperator = find(abs_data_ini1 > (min(abs_data_ini1) + max(abs_data_ini1)) * 3 / 4, 1);
% onlyear_part = data_ini0(1:seperator - 1000);
onlyear_part = data_ini1(1 : max(seperator-1000, datasize));
ofdm_part = data_ini1(seperator-110: end);

%%计算MIMO B 窃听器本振位置以及SNR，需要根据实际情况修改tmp的位置
dataB = onlyear_part(1:datasize);
figure;
fftshift_abs_fft_dataB = fftshift(abs(fft(dataB)));
plot(fest, fftshift_abs_fft_dataB);
title 无信号传输\_MIMOB
tmp = abs(fft(dataB));
tmp = tmp(1:35000);
[signalpower,max_idx]= max(tmp(1:900).^2);
noisepower = mean(tmp(15000:end).^2);
snrB = 10*log10(signalpower / noisepower);

%%包定位
payloadAB = read_complex_binary('0520_seperate/payload_streamAB');
mul = read_complex_binary('0520_seperate/beforeDemuxAB');
abs_mul = abs(mul);
seperator = find(abs_mul > (min(abs_mul) + max(abs_mul)) * 3 / 4, 1);
mul = mul(seperator-110:end);
mul = mul.';
ini = 0;
idx=-1;
while true
    tmp1 = payloadAB(64*ini+1:64*(ini+1));
    tmp2 = payloadAB(64*(ini+1)+1:64*(ini+2));
    tmp3 = payloadAB(64*(ini+2)+1:64*(ini+3));
    idx1 = strfind(mul(1:end), tmp1.');
    idx2 = strfind(mul(1:end), tmp2.');
    idx3 = strfind(mul(1:end), tmp3.');
    disp(idx1);
    disp(idx2);
    disp(idx3);
    if isempty(idx1) || isempty(idx2) || isempty(idx3)
        
    elseif (idx2 - idx1 == 80) && (idx3-idx2 == 80)
        idx = idx1;
        break
    end
    ini = ini + 1;
end
data_iniB = ofdm_part(idx-CP_length:idx-CP_length+per_OFDMsymbol_len*num_of_OFDMsymbol_per_packet -1);
% data_iniB = mul(idx-CP_length:idx-CP_length+per_OFDMsymbol_len*num_of_OFDMsymbol_per_packet -1);


eavesdropper_packets = zeros(1, num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len*num_of_packets);
options_lsq = optimoptions('lsqlin', 'Display','iter','FunctionTolerance',1e-10,'OptimalityTolerance',1e-29, 'StepTolerance',1e-29);

disp('start process');
%% 对于每个包的处理
for z = 1 : num_of_packets
    y1_CP = reshape(data_iniA((z-1)*num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len + 1 : z*num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len), per_OFDMsymbol_len, []);
    y1_subCP = y1_CP(CP_length+1 : end, :);

    
    y2_CP = reshape(data_iniB((z-1)*num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len + 1 : z*num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len), per_OFDMsymbol_len, []);
    y2_subCP = y2_CP(CP_length+1 : end, :);



    x1_OFDMsymbol = zeros(per_OFDMsymbol_len, num_of_OFDMsymbol_per_packet);
    for m = 1 : num_of_OFDMsymbol_per_packet % 一个packet里所有的OFDM符号

        OFDMsymbol = y1_subCP(:, m); % 每个接收OFDM符号
        C = zeros(NFFT, NFFT);
        for i = 1 : NFFT
            C(i, :) = exp(1j*2*pi*(f_std)*(i-1)/NFFT); % 标准值估a
        end
        [a1_OFDMsymbol] = lsqlin(C, OFDMsymbol*NFFT,[],[],[],[],[],[],[],options_lsq); % 最小二乘法估a
        a1_OFDMsymbol = a1_OFDMsymbol.';
        a1_OFDMsymbol(1) = 0;
        x1_OFDMsymbol(CP_length+1:end, m) = x_search(a1_OFDMsymbol, f_std);  % 根据估计的a和f重构

        % CP
        OFDMsymbol_CP = zeros(NFFT, 1);
        OFDMsymbol_CP(1 : NFFT-CP_length) = OFDMsymbol(1 : NFFT-CP_length);
        OFDMsymbol_CP(NFFT-CP_length+1 : NFFT) = y1_CP(1:CP_length, m);
        C = zeros(NFFT, NFFT);
        for i = 1 : NFFT
            C(i, :) = exp(1j*2*pi*(f_std)*(i-1)/NFFT);
        end
        [a1_OFDMsymbol] = lsqlin(C, OFDMsymbol_CP*NFFT,[],[],[],[],[],[],[],options_lsq); % 最小二乘法估a
        a1_OFDMsymbol = a1_OFDMsymbol.';
        a1_OFDMsymbol(1) = 0; % CP
        y1 = x_search(a1_OFDMsymbol, f_std);
        x1_OFDMsymbol(1:CP_length, m) = y1(NFFT-CP_length+1 : NFFT);
    end
    cancellation1 = y1_CP - x1_OFDMsymbol; % 接收信号与重构信号的差


    % 接收信号-天线2
    x2_OFDMsymbol = zeros(per_OFDMsymbol_len, num_of_OFDMsymbol_per_packet);
    for m = 1 : num_of_OFDMsymbol_per_packet

        OFDMsymbol = y2_subCP(:, m);
        C = zeros(NFFT, NFFT);
        for i = 1 : NFFT
            C(i, :) = exp(1j*2*pi*(f_std)*(i-1)/NFFT);
        end
        [a2_OFDMsymbol] = lsqlin(C, OFDMsymbol*NFFT,[],[],[],[],[],[],[],options_lsq); % 最小二乘法估a
        a2_OFDMsymbol = a2_OFDMsymbol.';
        a2_OFDMsymbol(1) = 0;
        x2_OFDMsymbol(CP_length+1:end, m) = x_search(a2_OFDMsymbol, f_std); % 根据估计的a和f重构

        % CP
        OFDMsymbol_CP = zeros(NFFT, 1);
        OFDMsymbol_CP(1 : NFFT-CP_length) = OFDMsymbol(1 : NFFT-CP_length);
        OFDMsymbol_CP(NFFT-CP_length+1 : NFFT) = y2_CP(1:CP_length, m);
        C = zeros(NFFT, NFFT);
        for i = 1 : NFFT
            C(i, :) = exp(1j*2*pi*(f_std)*(i-1)/NFFT);
        end
        [a2_OFDMsymbol] = lsqlin(C, OFDMsymbol_CP*NFFT,[],[],[],[],[],[],[],options_lsq); % 最小二乘法估a
        a2_OFDMsymbol = a2_OFDMsymbol.';
        a2_OFDMsymbol(1) = 0; % CP
        y2 = x_search(a2_OFDMsymbol, f_std);
        x2_OFDMsymbol(1:CP_length, m) = y2(NFFT-CP_length+1 : NFFT);
    end
    cancellation2 = y2_CP - x2_OFDMsymbol; % 接收信号与重构信号的差
% 
    cancellation1_fft = ((fft(reshape(cancellation1,1,[]))));
    cancellation2_fft = ((fft(reshape(cancellation2,1,[]))));
%     [a, ratio_point] = max(cancellation1_fft);
%     ratio = a/cancellation2_fft(ratio_point);
%     cancellation_mimo = cancellation1_fft - ratio*cancellation2_fft;
    [a, ratio_point] = max(cancellation2_fft);
    ratio = a/cancellation1_fft(ratio_point);
    cancellation_mimo = cancellation2_fft - ratio*cancellation1_fft;

    %画图
%     fest1_temp = Fs/length(cancellation2_fft);
    figure;
    fftshift_abs_cancellation1_fft = fftshift(abs(cancellation1_fft));
    semilogy(fest, fftshift_abs_cancellation1_fft);
    title 信号传输\_MIMOA消子载波旁瓣
    figure;
    fftshift_abs_cancellation2_fft = fftshift(abs(cancellation1_fft));
    semilogy(fest, fftshift_abs_cancellation2_fft);
    title 信号传输\_MIMOB消子载波旁瓣
%     figure;
%     plot(fest1, fftshift(abs(cancellation_mimo)));
%     title mimo消发射器本振
%     figure
%     plot(fest1, fftshift(abs(fft(reshape(y1_CP, 1, [])))));
%     title y1_CP
% 
%     ratio = max(abs(cancellation1_fft))/max(abs(cancellation2_fft));
%     cancellation_mimo = abs(cancellation1_fft) - ratio*abs(cancellation2_fft);
%     figure;
%     plot(fest1, fftshift(abs(cancellation_mimo)));
%     title mimo消发射器本振2
%     a = ifft(cancellation_mimo);
%     figure;
%     plot(fest1, fftshift(abs(fft(a))));


    eavesdropper_packets((z-1)*num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len + 1 : z*num_of_OFDMsymbol_per_packet*per_OFDMsymbol_len) = ifft(cancellation_mimo);

end


figure;
fftshift_abs_fft_eavesdropper_packets = fftshift(abs(fft(eavesdropper_packets)));
semilogy(fest, fftshift_abs_fft_eavesdropper_packets);
title 信号传输\_积累所有包提取窃听器本振

save('varible.mat' , 'abs_data_ini0','fftshift_abs_fft_dataA','abs_data_ini1' ,'fftshift_abs_fft_dataB', 'fftshift_abs_cancellation1_fft','fftshift_abs_cancellation2_fft','fftshift_abs_fft_eavesdropper_packets','cancellation2_fft','t','fest');


