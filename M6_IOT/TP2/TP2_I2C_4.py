from machine import Pin, SoftI2C
import time

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)

#valeur hexa de la réduction de 16 à 11bits
val=[0x3F8,0x3F7,0x0C8,0x7FF,0x738,0x648]

for i in range(len(val)):
    print("température en hex:", hex(val[i]))
    if (val[i] > 1023):
        res = (val[i] ^ 0b11111111111)+1
        temperature = - res * 0.125
    else :
        temperature = val[i] * 0.125
    print("température:",temperature)
    time.sleep(3)

# Expected output:
# température en hex: 0x3f8
# température: 63.5
# température en hex: 0x3f7
# température: 63.375
# température en hex: 0xc8
# température: 16.0
# température en hex: 0x7ff
# température: -0.125
# température en hex: 0x738
# température: 27.0
# température en hex: 0x648
# température: 18.0