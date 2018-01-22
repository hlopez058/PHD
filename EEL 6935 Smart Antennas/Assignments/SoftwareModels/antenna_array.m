%Time for Simulation
T=1;

%create an arriving signal
% fc: carrier frequency
% lc: carrier wavelength
% m: m(t) arriving signal 
% theta: angle of arrival (deg)
arvl_sig.fc = 2*10^9;
arvl_sig.lc = 3*10^8/arvl_sig.fc;
arvl_sig.m = 1; 
arvl_sig.theta = -90:1:90;

%build an antenna array
% M: number of antenna elements
% d: distance between elements
% D: multiplier of distance for each element
% S: array response vector for each theta
% W: weight vector designed
antn_arr.M = 5;
antn_arr.d = arvl_sig.lc/2;
antn_arr.D =0:1:antn_arr.M-1;
spacing = ((antn_arr.D'.*antn_arr.d)/arvl_sig.lc);
antn_arr.S = exp(-1i*2*pi*spacing*sind(arvl_sig.theta));

%Default weight vector
antn_arr.W=ones(1,antn_arr.M);

%Design a weight vector to nullout angles
antn_arr.e_thetas = [60,0,30,-75];
antn_arr.e = [1,0,0,0];
K=size(antn_arr.e,2)-1;
A=zeros(antn_arr.M,K+1);
for th_k = 1:1:K+1
    S_th_k = find(arvl_sig.theta==antn_arr.e_thetas(th_k));
    A(:,th_k)=antn_arr.S(:,S_th_k);
end
if antn_arr.M == (K+1) 
 antn_arr.W = antn_arr.e * inv(A);
end
if antn_arr.M > (K+1)
 antn_arr.W = antn_arr.e * pinv(A);
end
if antn_arr.M < (K+1)
 %statistical suppression 
end

%process anrenna array input signal
theta_idx = 1:1:size(arvl_sig.theta,2);
for t = T 
    for th=theta_idx
        processor.X = arvl_sig.m(t)* ... 
                        exp(1i*2*pi*arvl_sig.fc*t)* ...
                            antn_arr.S(:,th);
        processor.Y(th,t) = sum(ctranspose(antn_arr.W).*processor.X);
    end
end

%array beam pattern
G=(abs(processor.Y(:,t)).^2);
%array beam pattern
G_norm=(abs(processor.Y(:,t)).^2)/antn_arr.M;
%array beam pattern in dB
G_dB=10*log10(abs(processor.Y(:,t)').^2);
%array beam pattern in dB
G_dB_norm=10*log10((abs(processor.Y(:,t)).^2)/antn_arr.M);

plot(arvl_sig.theta,G_dB);
