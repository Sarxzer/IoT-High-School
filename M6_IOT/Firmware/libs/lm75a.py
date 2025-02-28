"""
Simple library to read temperature from LM75 sensor
"""

from machine import SoftI2C
import time

class lm75a:
    """
    Class to read temperature from LM75 sensor
    """
    def __init__(self, sda, scl, addr=0x48):
        self.i2c = SoftI2C(scl=scl, sda=sda, freq=100000, timeout=5000)
        self.addr = addr

    def read(self):
        """
        Read temperature from LM75 sensor
        """
        try:
            buf = bytearray(1)
            buf[0] = 0x00
            self.i2c.writeto(self.addr, buf)
            mesure = self.i2c.readfrom(self.addr, 2)
            val = (mesure[0] << 3)|(mesure[1] >> 5)
            temperature = val * 0.125
            return temperature
        except Exception as e:
            print('Error reading LM75 sensor:', e)
            return "Error"