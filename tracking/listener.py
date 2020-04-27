# TODO: get REP socket listening to port on guadr.gonzaga.edu

import time
import zmq

DEFAULT_PORT = "tcp://*:5555"
DEFAULT_FLEET_ENDPOINT = "tcp://localhost:5005"

class Listener(object):
    def __init__(self, port=DEFAULT_PORT, test_listen=True):
        self.port = port
        
        self.context = None
        self.socket = None
        self._bind_REP()

        if test_listen:
            self._updater_listen_test()
        
        listen_loop()


    def _bind_REP(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(self.port)
    
    def _updater_listen_test(self):
        """listen for requests on self.port and handle responses"""
        while True:
            msg = self.socket.recv()
            time.sleep(1)
            if msg == b"can you hear me?":
                self.socket.send(b"all ears")

    def listen_loop(self):
        """main loop for listening for messages, does not die"""
        while True:
            msg = self.socket.recv()
            self.send_updates_to_fleet(DEFAULT_FLEET_ENDPOINT, msg)
                       
    def send_updates_to_fleet(self, fleet_endpoint, msg):
        """gets received message from updaterand post results to zmq 
        endpoint that tracks fleet details.
            TODO: msg processing
        """
        context = zmq.Context()
        fleet_socket = context.socket(zmq.REQ)
        fleet_socket.connect(fleet_endpoint)

        socket.send(msg)
        resp = socket.recv()
        if resp == "success":
            print("successful fleet update")
        else:
            print("unsuccessful fleet update, see logs for details")

