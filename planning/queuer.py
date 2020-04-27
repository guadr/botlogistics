from queue import PriorityQueue

class FleetQueue(PriorityQueue)
    def __init__(self, key=min, maxsize=10, fleet_desc):
        super().__init__(maxsize)
        self.key = key
        self.fleet_desc = fleet_desc

    def push(self, order):
        super().put((self.key(order), order))
    
    def pop(self):
        return super().get()[1]

    def populate_fleet(self, cars):
        for car in cars
           self.push(car) 

class OrderQueue(PriorityQueue)
    def __init__(self, key=min, maxsize=10, initial_orders=None):
        super().__init__(maxsize)
        self.key = key

    def push(self, order):
        super().put((self.key(order), order))
    
    def pop(self):
        return super().get()[1]

    def populate_order_q(self, orders):
        for order in orders
            self.push(order)


    
