import os

from streamparse import Bolt, Stream


class MultiBolt(Bolt):
    outputs = [Stream(['value'], 'word'),
               Stream(['value'], 'number'),
               ]

    def initialize(self, conf, ctx):
        self.pid = os.getpid()

    def process(self, tup):
        word = tup.values.word
        if isinstance(word, int):
            self.emit([word],
                      stream='number')
        else:
            self.emit([word],
                      stream='word')


class TypeOne(Bolt):
    def initialize(self, conf, ctx):
        self.pid = os.getpid()

    def process(self, tup):
        self.logger.info("Type One bolt got a %s value", tup.values.value)


class TypeTwo(Bolt):
    def initialize(self, conf, ctx):
        self.pid = os.getpid()

    def process(self, tup):
        self.logger.info("Type Two bolt got a %s value", tup.values.value)
