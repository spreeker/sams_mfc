
import time


class Valve(object):

    def __init__(self, value):

        self.hisorry = []
        self.value = value

    def open(self):
        self.history.append(1)
        self.value = 1

    def close(self):
        self.history.append(0)
        self.value = 0


class Valve3(object):

    def __init__(self, value):

        self.history = []
        self.value

    def open_1(self):
        self.history.append(1)
        self.value = 1
        pass

    def open_2(self):
        self.history.append(2)
        self.value = 2
        pass
