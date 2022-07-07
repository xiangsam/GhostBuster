function [x] = x_search(a, f)
%X_SEARCH �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
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

