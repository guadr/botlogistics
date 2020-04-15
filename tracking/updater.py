# TODO: get REQ socket listening to port on guadr.gonzaga.edu

import time
import zmq

class Updater(object):
    DEFAULT_LOGGER_ENDPOINT = "tcp://localhost:5555"

    def __init__(self, endpoint=DEFAULT_LOGGER_ENDPOINT):
        self.target_endpoint = endpoint
        self.context = zmq.Context()
        
        self.socket = None

        self._connect()
        #assert self._test_connection_silent(), "unsuccessful connection to {}.".format(self.target_endpoint)
        self._test_connection()
         
    def _connect(self):
        self.socket = self.context.socket(zmq.REQ)

    def _test_connection_silent(self):
        """function to silently test socket connection to endpoint"""
        socket = self.context.socket(zmq.REQ)
        socket.connect(self.target_endpoint)
        # send test message
        socket.send(b"can you hear me?")
        # get response
        msg = socket.recv()
        if msg == b"all ears": 
            return True
        else:
            return False
        
    def _test_connection(self):
        """function to test socket connection and print debug or log info"""
        print("Attempting connnection to {}".format(self.target_endpoint))
        socket = self.context.socket(zmq.REQ)
        socket.connect(self.target_endpoint)

        # send test message
        start = time.time()
        socket.send(b"can you hear me?")
        # get response
        msg = socket.recv()
        end = time.time()
        print(f"response acquired: [ {msg} ] in {end-start} seconds.")
        if msg == b"all ears": 
            print("successful connection")
        else:
            print("unsuccessful connection")

