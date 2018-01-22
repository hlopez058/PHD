%% Linear Antenna Array Processor
% Hector Lopez EEL6935 SPRING2018
%%
theta=-90:90;

figure
Y3=processor(3,1,theta,false);
Y5=processor(5,1,theta,false);
Y10=processor(10,1,theta,false);
subplot(2,1,1);
plot(theta,Y3,theta,Y5,theta,Y10);
grid on;
title('Power Beam Pattern');
legend('M=3','M=5','M=10');
xlabel('Angle of Arrival (Degrees)');

Y3=processor(3,1,theta,true);
Y5=processor(5,1,theta,true);
Y10=processor(10,1,theta,true);
subplot(2,1,2);
semilogy(theta,Y3,theta,Y5,theta,Y10);
grid on;
axis([-90 90 0 100]);
title('Power Beam Pattern in dB');
legend('M=3','M=5','M=10');
xlabel('Angle of Arrival (Degrees)');


%% Processor(M,T)
% M=number of antenna elements in linear array
% T= maximum time window, max samples of time, T=1; t0.
% theta= 1d vector, angles(degree) of arrival for incoming signal
% dB=method of outputting the power beam pattern
function Y_theta = processor(M,T,theta,dB)
%carrier frequency
fc=2*10^9;
%speed of light
c=3*10^8;
%carrier wavelength
lambda_c =c/fc;
%optimum nyquist element spacing 
d=lambda_c/2;
dd=0:1:M-1;
D=dd*d;

%array response vector
%theta is a vector that will effect evey input x
%arriving unit signal for each sample of T 
m=ones(1,T);
%create unit vector array of weights
a = ones(1,M);
w=ctranspose(complex(a,0));

P=1:size(theta);
p=0;

for th = theta
    y=1:T;
    p=p+1;
    for t = 1:T
        S=exp(-1i*2*pi*(D/lambda_c)*sind(th));
        x=m(t)*exp(1i*2*pi*fc*t)*transpose(S);
        xw=x.*w;
        y(t)=sum(xw);
    end
    %Y=trapz(y);
    Y=y;
    if(dB==true)
        i=10*log10(abs(Y)^2);
        if(i>1)
            P(p)=i;
        else
            P(p)=0;
        end
    else
        P(p)=abs(Y)^2;
    end
end
Y_theta=P;
end



%%%%
%% ZeroForcing Beam Former
% Hector Lopez EEL6935 SPRING2018
% Assignment 1.b

M=4;
thetas = [60,0,30,-75];
d=0:1:M-1;
e=[1,0,0,0];
A = exp(-1i*2*pi*(d'/2)*sind(thetas));
w_H=e*inv(A);
w=ctranspose(w_H);

m0=1;t=0;fc=1;k=0;
Y=1:size(th_sweep);
th_sweep=-90:0.1:90;
for th = th_sweep
    k=k+1;
    S=exp(-1i*2*pi*(d'/2)*sind(th));
    x=m0*exp(1i*2*pi*fc*t)*transpose(S);
    Y(k)=sum(w_H.*x);
end

%Power Beam Pattern
P=abs(Y).^2;
P_dB=10*log10(abs(Y).^2);
%Plot Results
figure;
close all;
subplot(2,1,1);
plot(th_sweep,P);
grid on;
title('ZeroForcing BeamFormer - Power Beam Pattern dB');
xlabel('Angle of Arrival (Degrees)');
ylabel('Power');

subplot(2,1,2);
plot(th_sweep,P_dB);
ylim=[-50 20];
set(gca,'YLim',[-50 20])
grid on;
title('ZeroForcing BeamFormer - Power Beam Pattern dB');
xlabel('Angle of Arrival (Degrees)');
ylabel('Power');
