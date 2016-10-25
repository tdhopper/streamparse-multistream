from itertools import cycle
from time import sleep

from streamparse import Spout


class ValueSpout(Spout):
    outputs = ['word']

    def initialize(self, stormconf, context):
        self.values = cycle(['dog', 'cat', 'zebra', 'elephant', 1, 2, 3, 4])

    def next_tuple(self):
        value = next(self.values)
        self.emit([value])
        sleep(.3)
