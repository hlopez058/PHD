import numpy as np
import math
class EV(object):
    def __init__(self,ID, timeout):
        self.ID = ID
        self.timeout = timeout
        self.wait_time = 0
    def wait(self, delay=1):
        self.wait_time += delay
    def arriving(t,timeout):
        EVs=[]
        for i in np.arange(EV.demand_curve(t)):
            EVs.append(EV(f"EV-{t}.{i}",timeout))
        return EVs
    def demand_curve(t):
        #if t<5 :
        #    return t+1
        #if t>=5: 
        #    return 1
        avg_cnt_of_ev = 4
        return avg_cnt_of_ev*math.cos(t*(20/math.pi)) + (avg_cnt_of_ev/2)
            
class Lobby(object):
    def __init__(self):
        self.EVs = []
    def enter(self,EVs):
        self.EVs.extend(EVs)
    def leave(self,EV):
        self.EVs.remove(EV)
    def get_next(self):
        if len(self.EVs) > 0:
            return self.EVs.pop(0)
        else:
            pass
    def is_not_empty(self):
        return len(self.EVs) > 0
    def update(self):
        [ev.wait() for ev in self.EVs]
        timedout = [ev for ev in self.EVs if ev.wait_time >= ev.timeout]
        [ self.leave(ev) for ev in timedout ]
        return timedout

class Bay(object):
    def __init__(self,ID,swap_delay):
        self.ID = ID
        self.swap_delay = swap_delay
        self.timer = 0
        self.EV=None
    def is_empty(self):
        return self.EV is None
    def enter(self,EV):
        self.EV = EV
    def leave(self):
        ev = self.EV
        self.EV = None
        return ev
    def update(self):
        if self.EV is not None:
            if self.timer < self.swap_delay:
                self.EV.wait()
                self.timer += 1
            else:
                self.timer = 0
                return self.leave()
        return None  
    def create(count,swap_delay):
        bays=[]
        for i in range(count):
            bays.append(Bay(f"Bay{i}",swap_delay))    
        return bays

class Reporting(object):
    def __init__(self):
        self.data = []
    def capture(self, element):
        if element is not None :
            self.data.append(element)
    def capture_all(self, elements):
        e = [e for element in elements if element is not None]
        self.data.extend(e)
    
def main():
    lobby = Lobby()
    bays = Bay.create(count=3,swap_delay=1)
    T = 720
    serviced = []
    unserviced =[]
    ev_timeout = 5
    
    report_arrival = Reporting()
    report_attrition = Reporting()
    report_servicing = Reporting()

    for t in range(T):
        lobby.enter(EV.arriving(t,ev_timeout))
        report_arrival.capture(len(EV.arriving(t,ev_timeout)))
        [bay.enter(lobby.get_next()) for bay in bays if bay.is_empty and lobby.is_not_empty]
        svcd = [ bay.update() for bay in bays ]
        serviced.extend(svcd)
        report_servicing.capture(len(svcd))
        left = lobby.update()
        unserviced.extend(left)
        report_attrition.capture(len(left))
            
    #[ print(f"{ev.ID}: {ev.wait_time}t waited") for ev in serviced if ev is not None]
    #[ print(f"{ev.ID}: {ev.wait_time}t waited and left") for ev in unserviced if ev is not None]
    
    import matplotlib.pyplot as plt
    plt.plot(report_arrival.data, label = "arrivals")
    plt.plot(report_servicing.data, label = "servicing")
    plt.plot(report_attrition.data, label = "attrition")
    plt.title('EV Daily Demand for Battery Swapping (Events)')
    plt.legend()
    plt.show()


main()
