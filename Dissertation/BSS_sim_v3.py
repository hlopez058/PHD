import matplotlib.pyplot as plt
import random
import math


class EV(object):
    def __init__(self,ID,timeout):
        self.ID = ID
        self.timeout = timeout
        self.counter = 0
        self.is_done = False
    def done():
        self.counter>= self.timeout

def demand(t):
    curve = t
    evs = []
    for i in range(max(0,int(curve))):
        evs.append(EV("EV",2))
    return evs

T = 1440 # minutes in day
Bays = 2 # bays to swap battery
q = []
w = []
for t in range(T):
    arrived = demand(t)
    [ q.append(ev) for ev in arrived]
    [ w.append(q.pop(0)) for i in range(Bays) if len(w) < Bays and len(q) > 0] 
    done = [ ev for ev in w if ev.done ]

print("done")

plt.plot(P, label = "arrivals")
plt.plot(L, label = "pending")
plt.title('EV Battery Swapping Arrivals')
plt.legend()
plt.show()



