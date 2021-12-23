


import random

class _helper_():
    def get_curve_or_model(self,t,curve,model):
        if len(curve) > t:
            return curve[t]
        else :
            return model
 

class Prosumer(_helper_):
    def __init__(self,id,kwh): 
        self.id =id
        self.gen_curve = []
        self.load_curve = []
        self.plant = Plant(kwh)

    def get_consumption(self,t):
        return self.get_curve_or_model(t,self.load_curve,random.randint(0, 1000))

    def set_consumption_curve(self,load_curve):
        self.load_curve = load_curve

    def get_production(self,t):
        return self.get_curve_or_model(t,self.gen_curve,self.plant.output(t))

    def set_production_curve(self,gen_curve):
        self.gen_curve = gen_curve
    
    def net_production(self,t):
        return max(self.get_production(t) - self.get_consumption(t),0)


class Plant():
    def __init__(self,capacity):
        self.capacity =capacity
    def output(self,t):
        generators = [random.randint(0, 500),random.randint(0, 500)]
        return min(self.capacity,sum(generators))
    
def get_prosumers(amount):
    prosumers = []
    for i in range(amount):
        prosumer = Prosumer(i+1,kwh=500)
        prosumers.append(prosumer)
    return prosumers

def set_prosumer_curves(prosumers):
    load_curve = [1,2,3,4,5,6,7,8,9,10,9,8,7,5,4,3,2,1]
    gen_curve = [1,2,1,4,1,9,9,8,9,10,9,9,9,9,4,3,2,1]
    for prosumer in prosumers:
        prosumer.set_consumption_curve(load_curve)
        prosumer.set_production_curve(gen_curve)
    return prosumers



def main():
    N = 3
    T = 24
    prosumers  = get_prosumers(N)
    #mannually upload curves for each prosumer from a file?
    #prosumers = set_prosumer_curves(prosumers)
    for t in range(T):
        x = [f"Prosumer{prosumer.id}: {prosumer.net_production(t)}" for prosumer in prosumers]
        print(f"t={t}: {x}")

if __name__ == "__main__":
    main()