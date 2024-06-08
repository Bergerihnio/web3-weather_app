# from w1thermsensor import *
import random

# sensor = W1ThermSensor()

def get_temperature():
    temperature = random.randrange(3, 9)
    # temperature = sensor.get_temperature()
    return temperature

if __name__ == '__main__':
    get_temperature()

# Temperature sensor model -> DS18B20

