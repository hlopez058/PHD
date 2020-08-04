

class Bays(object):
    def __init__(self,count,timeout):
        self.bays = []
        self.count = count
        for i in range(count):
            b = Bay(timeout)
            self.bays.append(b)
        
    def work(self):
        for i in range(len(self.bays)):
            if self.bays[i].EV is not None:
                self.bays[i].work() 

    def recieve(self,EVs):
        for i in range(len(self.bays)):
            if self.bays[i].EV is not None:
                if len(EVs) > 0 :
                    ev = EVs.pop(0)
                    self.bays[i].recieve(ev)
                    print(f"added an ev to bay{self.bays[i]}")
    def done(self):
        dones = []
        for i in range(len(self.bays)):
            if self.bays[i].done :
                dones.append(self.bays[i].EV) 
        return dones

class Bay(object):
    def __init__(self,timeout):
        self.EV = None
        self.done = False
        self.timeout = timeout
        self.counter = 0
    def work(self):
        self.counter += 1
        self.EV.wait()
        if self.counter >= self.timeout:
            self.done = True
    def recieve(self,EV):
        self.counter = 0
        self.EV = EV

class Lobby(object):
    def __init__(self):
        self.EVs = []
    def add(self,EV):
        self.EVs.append(EV)
    def get(self,count):
        return [ self.EVs[0] for ev in range(count) if len(self.EVs) > 0]
    def wait(self):
        if len(self.EVs) > 0:
            for i in range(len(self.EVs)):
                self.EVs[i].wait()
    def left(self):
        self.EVs = [ev for ev in self.EVs if not ev.timedout()]
        return self.EVs

class EV(object):
    def __init__(self,ID,timeout):
        self.ID = ID
        self.counter = 0
        self.timeout = timeout
    def wait(self,t=1):
        self.counter += 1
    def arrive(t,timeout):
        EVs = []
        demand = EV.demand(t,5)
        for i in range(demand):
            ev = EV(f"EV-i",timeout)
            EVs.append(ev)
        return EVs
    def demand(t,demand,variance=1):
        avg_cnt_of_ev = demand * random.uniform(1,variance)
        return int(max(0,avg_cnt_of_ev*math.cos(t*(20/math.pi)) + (avg_cnt_of_ev/2)))
    def timedout(self):
        return self.counter >= self.timeout

lobby = Lobby()
bays = Bays(3,timeout=2)
serviced= []
unserviced =[]
T =1440
for t in range(T):
    lobby.add(EV.arrive(t,timeout=10))
    bays.recieve(lobby.get(bays.count))
    bays.work()
    done = bays.done()
    serviced.extend(done) 
    lobby.wait()
    unserviced.extend(lobby.left())

import matplotlib.pyplot as plt
plt.plot(serviced, label = "serviced")
plt.plot(unserviced, label = "unserviced")
plt.title('EV Battery Swapping Arrivals')
plt.legend()
plt.show()
