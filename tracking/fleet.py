# TODO: make a persistent db for storing fleet details
import zmq
import sqlite3


class Fleet(object):
    FLEET_TCP_IP = "tcp://*"
    FLEET_TCP_PORT = "5005"

    FLEET_BACKEND = "sqlite loc"
    
    def __init__(self, cars=None, load_from_db=True):
        """
         args:
            cars: dictionary of cars
                key: string that represents a car ID
                value: instance of CarAttributes
        """
        if load_from_db:
            print("initalizing self.cars from db")
            self.cars = self._init_fleet_from_db()
        else:
            self.cars = cars

    def _init_fleet_from_db(self):
        # TODO
        print("opening db...")
        return {}

    def fleet_update_listener(self):
        """listen on tcp port for car updates"""

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(Fleet.FLEET_TCP_IP + Fleet.FLEET_TCP_PORT) 

        while True:
            #  Wait for next request from client
            new_car_info = socket.recv()
            print("Received update on a cars info: %s" % new_car_info)
            time.sleep(1)
            new_car_info = new_car_info.split(",")
            self.update_fleet(new_car_info)

    def update_cars(self, new_car_info):
        """update cars according to new_car_info"""
        self.cars[new_car_info[0]] = (new_car_info[1], new_car_info[2:])

    
class CarAttributes(object):
    """Class to store information about each car in fleet"""

    def __init__(self, attributes):
        self.items = attributes


if __name__ == "__main__":
    """example of Fleet/CarAttributes usage"""

    # create fake car data to spoof for testing
    cars = {}
    cars["car1"] = CarAttributes(
        [("lat", 47.71),
         ("long", 33.54),
         ("destination", "hk_east"),
         ("order", "starbucks", "sandwich", "coffee"),
         ("status", "enroute")
        ]
    )
    cars["car2"] = CarAttributes(
        [("lat", 47.74),
         ("long", 33.53),
         ("destination", "hemm_sw"),
         ("order", None),
         ("status", "idle")
        ]
    )

    # create fleet
    f = Fleet(cars)
    f.fleet_update_listener()
