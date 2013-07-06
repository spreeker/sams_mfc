
import time
# import settings
import fake_sensors
import actuators
# current sensor?

ph_valve = actuators.Valve(0)


sensors = {

    'v-pressure-a': {},
    'v-pressure-b': {},

    'v-monster-a': {},
    'v-monster-c': {},

    'v-ph-up': {},
    'v-ph-down': {},

    'v-gas-a': {},
    'v-gas-c': {},

    'v-influent-a': {},
    'v-influent-c': {},

    'pump-influent-a': {},
    'pump-influent-c': {},

    'pump-a': {},
    'pump-c': {},

    'ph-sensor-a': fake_sensors.FakePH_A(7,  1.5),

    'ph-sensor-c': fake_sensors.FakePH_C(7),

    'voltage-sensor': {},

    'pm-sensor-a': {},
    'pm-sensor-c': {},

    'methane-sensor-a': {},
    'methane-sensor-c': {},

    'liquiphant-a': {},
    'liquiphant-c': {},

}


def main_loop():

    while True:
        #check gas a
        check_gas('a')
        #check gas c
        check_gas('b')

        # check ph a
        # check ph c

        # check pressure a
        # check pressure c

        # check voltage

        # check influent

        # make new fake sensor values

        time.sleep(0.1)


# keep
samples = []

methane_values = []

def check_gas(compartment):
    """
    Check if we need to open gas valve
    """
    # read liquiphant
    lqh = sensors.get('liquiphant-%s' % compartment)
    #value = lqh.read()
    # avg samples

    valve = sensors.get('v-gas-%s' % compartment)

    if avg_value > 0.8:
        #open valve
        valve.open()
        # store methane sensor value
        # methane_values.append((compartment, value))
    else:
        #close_valve
        valve.close()


ph_actions = {

    'opened': '',
    'closed': '',

    'measurements': []
}


def check_ph(compartment):
    """
    Check if we need to adjust to keep ph levels within
    boundaries
    """

    min_ph = 0.5
    max_ph = 1

    ph_s = sensors.get('ph-sensor-%s' % compartment)
    value = ph_s.get_value()

    if value < min_ph:
        pass
        # open ph up
        # close ph up
    elif value > max_ph:
        # open ph down
        # close ph up
        pass
    else:
        # do nothing
        pass

pressures = []


def check_pressure(compartment):
    """
    Make sure pressure is constant
    """
    min_pressure = 0.7
    target = 0.75
    max_pressure = 0.8

    valve_position = 0.5

    correction = 0.1

    p_s = sensors.get('pressure-sensor-%s' % compartment)
    pressure = p_s.read()

    v_pressure = sensors.get('v-pressure-%s' % compartment)

    if pressure < min_pressure:
        # open up valve with correction
        pass
    elif pressure > max_pressure:
        # close valve with correction
        pass
    elif target - 0.05 > pressure > target + 0.05:
        pass
        # Do nothing.

voltage_messurements = []



currents = []


def check_voltage():
    """
    """
    # messure voltage
    pass


def check_influent_a():
    """
    Check influent depending on

    a + c methane / current
    """
    pass
    influent_valve = sensors.get('v-influent-a')
    influent_valve.open(0.5)


def check_influent_c():
    """
    Check influent depending on

    ph / gas / voltage
    """
    pass
