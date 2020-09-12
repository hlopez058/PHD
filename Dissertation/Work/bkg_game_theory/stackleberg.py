
from sympy import * 


init_printing()

firms = 3
print(f"Stackleberg Game with {firms} firms.")
# Total Market Quantity Demand
q = [symbols('q%d'% i) for i in range(firms)]

Q = sum(q[i] for i in range(firms))

pprint(Q)

# Market Demand Curve
a,b = symbols('a,b')
a = 120
b = 0.5
P = a - b * Q

pprint(P)

# Total Revenue
TR = [symbols('TR%d'% i) for i in range(firms)]
for i in range(firms):
    TR[i]= expand(P * q[i])
    print(f"TR_{i}:")
    pprint(TR[i])


# Marginal Revenue
MR = [symbols('MR%d'% i) for i in range(firms)]
for i in range(firms):
    MR[i]= Derivative(TR[i],q[i]).doit()
    print(f"MR_{i}")
    pprint(MR[i])
    
# Marginal Cost
MC = [symbols('MC%d'% i) for i in range(firms)]
for i in range(firms):
    MC[i]=20 + i*2
    print(f"MC_{i}")
    pprint(MC[i])

# Reaction Functions :
qq = [symbols('qq%d'% i) for i in range(firms)]
for i in range(firms):
    qq[i]=solve(MR[i] - MC[i],q[i])[0]
    print(f"q*_{i}:")
    pprint(qq[i])

# Response Functions :
# The leader takes into account all the reactions
# create a leader response to the reactions
P_0 = P # Leaders market demand in terms of leader quantity
for i in range(firms - 1) :
    P_0 = P_0.subs(q[i+1],qq[i+1])

print(f"Leader Demand:")
pprint(P_0)

TR_0 = expand(P_0 * q[0])
print(f"Leader Total Revenue:")
pprint(TR_0)

MR_0 = Derivative(TR_0,q[0]).doit()
print(f"Leader Marginal Revenue:")
pprint(MR_0)

print(f"Leader Marginal Cost:")
MC_0 = MC[0]

# Most profit maximizing quantity for leader is q_0
q_0 = solve(MR_0-MC_0,q[0])[0]
print(f"Leader Most Profitable Quantity:")
pprint(q_0)

# Reactions Taken :
qqq = [symbols('qqq%d'% i) for i in range(firms)]
for i in range(firms-1):
    qqq[i]=qq[i+1].subs(q[0],q_0)
    print(f"Quantity Response of q{i+1} to Leader:")
    pprint(qqq[i])
