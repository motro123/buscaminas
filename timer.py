from datetime import datetime

import time

class Timer(object):
    """A simple timer class"""



    def __init__(self):
        pass



    def start(self):
        self.inicio = time.time()




    def elapsed(self):
        t = time.time()
        return int(t - self.inicio)

