# from w1thermsensor import *
import random

# sensor = W1ThermSensor()

def get_temperature():
    temperature = random.randrange(5, 25) # only for testZSD
    # temperature = sensor.get_temperature()
    return f'{temperature:.2f}'

if __name__ == '__main__':
    get_temperature()

# Temperature sensor model -> DS18B20

