import random

# global related data..
context = {
    'shared_data': 0
}


class Sensor(object):
    """
    Sensor object
    """

    def value(self):
        """
        get current value
        """
        raise NotImplementedError


class FakePH_A(Sensor):
    """
    fake ph sensor Anode
    """
    dPH = 0.5

    def __init__(self, init_value, valve, current):
        self.valve = valve
        self.value = init_value

    def value(self):
        """

        """
        pass
        # if valve open ph down
        # if valve close ph up
        # current * ..
        return self.value


class PakePH_C(Sensor):
    """
    fake ph sensor Cathode
    """
    def __init__(self, init_value, min_v=6, max_v=8, delta=1):
        """
        ..
        """
        self.value = init_value
        self.min_v = min_v
        self.max_v = max_v
        self.delta = 1

    def value(self):
        """
        change value a random bitsy..
        """
        if self.value < self.min_v:
            delta = 1
        elif self.value > self.max_v:
            delta = -1

        self.value += random.random() * delta
        return self.value
