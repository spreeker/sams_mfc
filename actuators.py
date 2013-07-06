

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
