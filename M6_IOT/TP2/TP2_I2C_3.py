from machine import Pin, SoftI2C
import time

# configuration du bus I2C sur l'ESP8266.
# le timeout est nécessaire pour eviter l'erreur watch dog si pas de réponse sur le Bus.

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)

while True:
    buf = bytearray(1) # création d’un buffer 1 octet
    buf[0] = 0x00 # adresse du registre point
    i2c.writeto(0x48, buf) # écriture dans le LM75
    mesure = i2c.readfrom(0x48, 2) # lecture
    print("température en bin:", bin(mesure[0]), bin(mesure[1]))
    val = (mesure[0] << 3)|(mesure[1] >> 5) #reduction de 16 à 11bits.
    print(val)
    temperature = val * 0.125
    print("température:", temperature)
    time.sleep(3)
