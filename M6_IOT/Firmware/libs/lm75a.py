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
            buf = bytearray(1) # création d’un buffer 1 octet
            buf[0] = 0x00 # adresse du registre point
            self.i2c.writeto(0x48, buf) # écriture dans le LM75
            mesure = self.i2c.readfrom(0x48, 2) # lecture
            
            mesure_int = (mesure[0] << 8) | mesure[1]
            
            print("temperature en hex:", hex(mesure_int))
            print("temperature en bin:", bin(mesure_int))

            # Convert to 11-bit signed value
            mesure = mesure_int >> 5  # Reduction de 16 à 11 bits

            if (mesure > 1023):
                res = (mesure ^ 0b11111111111)+1
                temperature = - res * 0.125
            else :
                temperature = mesure * 0.125
            print("temperature:",temperature)
            time.sleep(3)
            return temperature
        except Exception as e:
            print('Error reading LM75 sensor:', e)
            return "Error"