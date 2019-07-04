function [w,b]=perceplearn(P,t,w,b,ep)
clc; close all
% P  = Input Vector
% w  = Weight
% b  = bias
% T  = Target Vector
% ep = Epoches  (No. of max iterations)
% Perceptron Learning Rule is:
% Wnew = Wold + e*p
% e    = t - a
% b    = bold + e
% Update the weight & bias until it prodeuces correct target for inputs.
% For example:
% And Gate: 
% P=[0 0 1 1; 0 1 0 1]; t=[0 0 0 1]; w=[0 0]; b=0; ep=20;
% [w b]=perceplearn(P,t,w,b,ep);
%
% OR Gate: 
% P=[0 0 1 1; 0 1 0 1]; t=[0 1 1 1]; w=[0 0]; b=0; ep=20;
% [w b]=perceplearn(P,t,w,b,ep);
%
% XOR Gate: (Limitation of Perceptron)
% P=[0 0 1 1; 0 1 0 1]; t=[0 1 1 0]; w=[0 0]; b=0; ep=10;
% [w b]=perceplearn(P,t,w,b,ep);
plotpv(P,t)
linehandle = plotpc(w,b); grid on
[r c]=size(P);
chk=0; iter=0;
while chk~=5
    for i=1:c        
        a=hardlimit(w*P(:,i)+b); % Evaluating Network
        chk=chk+1;
        if chk==5
            break; % If w and b are adjusted as required.            
        end        
        if a~=t(i)
            chk=0;
            e=t(i)-a;
            w=w+(e*P(:,i)');
            b=b+e;
        end
        pause(0.2)
        linehandle = plotpc(w,b,linehandle);  drawnow;        
    end
    iter=iter+1
    if iter==ep
         disp('Maximum Iterations Reached');       
        break;       
    end
end
disp('=============================================================')
disp('To verify the w and b for given input and targets Run following:')
disp('T=evalnet(P,w,b);')
