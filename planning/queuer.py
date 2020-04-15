from queue import PriorityQueue

class FleetQueue(object):
    def __init__(self, fleet_ats):
        self.fleet_ats = fleet_ats
        self.q = PriorityQueue()


    
