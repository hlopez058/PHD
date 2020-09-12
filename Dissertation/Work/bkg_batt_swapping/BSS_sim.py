import numpy as np
import math
import random
class EV(object):
    def __init__(self,ID,waiting_limit,variance=1):
        self.ID = ID
        self.waiting_limit = waiting_limit*random.uniform(1, variance)
        self.wait_time = 0
    def wait(self, delay=1):
        self.wait_time += delay
    def arriving(t,
    demand,
    waiting_limit,
    demand_variance=1,
    waiting_limit_variance=1):
        EVs=[]
        for i in np.arange(EV.demand_curve(t,demand,demand_variance)):
            EVs.append(EV(f"EV-{t}.{i}",
            waiting_limit,waiting_limit_variance))
        return EVs
    def demand_curve(t,demand,variance=1):
        avg_cnt_of_ev = demand * random.uniform(1,variance)
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
    def is_not_empty(self):
        return len(self.EVs) > 0
    def update(self):
        [ev.wait() for ev in self.EVs]
        timedout = [ev for ev in self.EVs 
        if ev.wait_time >= ev.waiting_limit]
        [ self.leave(ev) for ev in timedout ]
        return timedout

class Bay(object):
    def __init__(self,ID,swap_delay,variance=1):
        self.ID = ID
        self.swap_delay = swap_delay*random.uniform(1, variance)
        self.timer = 0
        self.EV=None
    def enter(self,EV):
        self.EV = EV
    def leave(self):
        ev = self.EV
        self.EV = None
        return ev
    def is_empty(self):
        return self.EV is None
    def update(self):
        if self.EV is not None:
            if self.timer < self.swap_delay:
                self.EV.wait()
                self.timer += 1
            else:
                self.timer = 0
                return self.leave()
    def create(count,swap_delay,variance):
        bays=[]
        for i in range(count):
            bays.append(Bay(f"Bay{i}",
            swap_delay,variance))    
        return bays

class Reporting(object):
    def __init__(self):
        self.data = []
    def capture(self, element):
        if element is not None :
            self.data.append(element)
    def capture_all(self, elements):
        e = [e for element in elements 
        if element is not None]
        self.data.extend(e)


def results(report):
    import matplotlib.pyplot as plt
    plt.plot(report['arrival'].data, label = "arrivals")
    plt.plot(report['serviced'].data, label = "servicing")
    plt.plot(report['unserviced'].data, label = "attrition")
    plt.title('EV Daily Demand for Battery Swapping (Events)')
    plt.legend()
    plt.show()


def main():
    report = {
        'arrival' : Reporting(),
        'unserviced' : Reporting(),
        'serviced' : Reporting()
    }
    lobby = Lobby()
    bay_swap_delay = 0
    bay_count = 5
    ev_avg_demand = 5
    ev_waiting_limit = 5
    bays = Bay.create(count=bay_count,
    swap_delay=bay_swap_delay,
    variance=1)
    T = 1440

    for t in range(T):
        # EV's arrive to the station
        arriving = EV.arriving(t,
        demand=ev_avg_demand,
        waiting_limit=ev_waiting_limit,
        demand_variance=1,
        waiting_limit_variance=1)
        # EV's enter a lobby to wait to be serviced
        lobby.enter(arriving)
        report['arrival'].capture(len(lobby.EVs))
        # EV's move from the lobby into available bays
        [bay.enter(lobby.get_next()) for bay in 
        bays if bay.is_empty and lobby.is_not_empty]
        # EV's are serviced in the bay until swap delay
        done = [svcd for svcd in 
        [ bay.update() for bay in bays] 
        if svcd is not None]
        report['serviced'].capture(len(done))
        # EV's that wait to long leave the lobby
        left = lobby.update()
        report['unserviced'].capture(len(left))
            
    results(report)
    #print(f"Number of Bays {bay_count}")
    #print(f"Number of periods/mins to service EV's t={T}")
    #print(f"Delay in swapping battery {bay_swap_delay} periods (t)")
    #print(f"Number of EV's serviced {sum(report['serviced'].data)}")
    #print(f"Number of EV's unserviced {sum(report['unserviced'].data)}")
    #print(f"Total Number of EV demand {sum(report['arrival'].data)}")

    print(f"T Periods,Bays,Swap Delay,EV Timeout,Serviced,Unserviced,Total EV's")
    print(f"{T},{bay_count},{bay_swap_delay},{ev_waiting_limit},{sum(report['serviced'].data)},{sum(report['unserviced'].data)},{sum(report['arrival'].data)}")

    

main()

