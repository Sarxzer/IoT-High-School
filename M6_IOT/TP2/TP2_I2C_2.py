from machine import Pin, SoftI2C
import time

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)

while True:
    buf = bytearray(1) # création d’un buffer 1 octet
    buf[0] = 0x48 # adresse du registre point
    i2c.writeto(0x48, buf) # écriture dans le LM75
    mesure = i2c.readfrom(0x48, 2) # lecture
    print("température en bin:", bin(mesure[0]), bin(mesure[1]))
    print("température en hex:", hex(mesure[0]), hex(mesure[1]))
    print("température en dec", mesure[0], mesure[1])
