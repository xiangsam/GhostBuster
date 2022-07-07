function [x] = x_search(a, f)
%X_SEARCH 此处显示有关此函数的摘要
%   此处显示详细说明
NFFT = length(a);
x = zeros(1, NFFT);
f = real(f);
for n = 1 : NFFT
    for k = 1 : NFFT
        x(n) = x(n) + a(k)*exp(1j*2*pi*f(k)*(n-1)/NFFT);
    end
end
x = x/NFFT;
x = x.';
end

