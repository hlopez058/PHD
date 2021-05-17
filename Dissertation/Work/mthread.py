# System modules
from queue import Queue
from threading import Thread
import time
import threading
import random

class AtomicCounter(object):
    """An atomic, thread-safe counter"""

    def __init__(self, initial=0):
        """Initialize a new atomic counter to given initial value"""
        self._value = initial
        self._lock = threading.Lock()

    def inc(self, num=1):
        """Atomically increment the counter by num and return the new value"""
        with self._lock:
            self._value += num
            return self._value

    def dec(self, num=1):
        """Atomically decrement the counter by num and return the new value"""
        with self._lock:
            self._value -= num
            return self._value

    @property
    def value(self):
        return self._value


# Set up some global variables
counter = AtomicCounter()
num_fetch_threads = 2
order_queue = Queue()
items_queue = [1,2,3,4,5,6]

def processOrders(i, q, max_t):
    while True:
        time.sleep(1)
        # increase the global timestep
        counter.inc(1)
        print(f'Processing Order {order} at HE{counter.value}\n')
        order = q.get()        
        q.task_done()
        
def simulateBuyer(i, q):
    # instantiate a new buyer object
    # begin a live game with the buyer
    time.sleep(random.randrange(1,2))
    print(f'Buyer-{i}: Placing order at HE{counter.value}\n')
    q.put(f'order-from-Buyer{i}')    
    #q.task_done()

# Set up a thread for each buyer to read the items list 
# and submit an order to orders queu
for i in range(3):
    buyer_simulation = Thread(target=simulateBuyer, args=(i, order_queue,))
    buyer_simulation.setDaemon(True)
    buyer_simulation.start()

# Set up some threads to process orders
for i in range(1):
    worker = Thread(target=processOrders, args=(i, order_queue,10))
    worker.setDaemon(True)
    worker.start()


        
# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
print('\n*** Main thread waiting')
order_queue.join()
print('\n*** Done')
print(f'remaining orders {order_queue.qsize()}')



