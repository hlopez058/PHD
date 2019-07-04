import math

def sigmoid(x):
    return (1/(1+(math.exp(-x))))

j=0.8*0.9 + 0.6*1 + 0.1*0.9
J0 = sigmoid(0.3*0.8 + 0.3*1 + 0.7*0.9)
J1 = sigmoid(0.8*0.9 + 0.6*1 + 0.1*0.9)

print(j)
print(J0)
print(J1)

O0 = 0.9*J0 + 0.4*J1
O1 = 0.2*J0 + 0.1*J1

print(O0)
print(O1)
print(sigmoid(0.88066)*(1-sigmoid(0.88066)))