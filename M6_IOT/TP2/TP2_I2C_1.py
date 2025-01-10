from machine import Pin, SoftI2C
import time
#configuration du bus I2C.
#le timeout est nécessaire pour eviter l'erreur watch dog si pas de réponse sur le Bus.
i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000,
timeout=5000)

print ("scan du bus i2c")
devices = i2c.scan() #rangement des adresses des périphériques dans une list.

if len(devices) == 0: #vérification si il y a au moins un périphérique
    print("aucun périphérique sur le bus I2C")
else :     #affichage des adresses des périphériques présent.
    print("périphérique trouvé:",len(devices))
    for i in devices:
        print("decimal", i)
        print("hexadecimal", hex(i))