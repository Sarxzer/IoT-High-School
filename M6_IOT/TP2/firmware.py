from machine import Pin, SoftI2C
import time
import ssd1306

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)

test_values = [0x3F8,0x3F7,0x0C8,0x7FF,0x738,0x648]

while True:
    buf = bytearray(1) # création d’un buffer 1 octet
    buf[0] = 0x00 # adresse du registre point
    i2c.writeto(0x48, buf) # écriture dans le LM75
    mesure = i2c.readfrom(0x48, 2) # lecture
    val = (mesure[0] << 3)|(mesure[1] >> 5) #reduction de 16 à 11bits.
    if (val > 1023):
        res = (val ^ 0b11111111111)+1
        temperature = - res * 0.125
    else :
        temperature = val * 0.125
    oled.fill(0)
    oled.text("Temp:" + str(temperature) + "C", 0, 0)
    oled.show()
    time.sleep(3)

# Test loop
# for val in test_values:
#     if (val > 1023):
#         res = (val ^ 0b11111111111)+1
#         temperature = - res * 0.125
#     else :
#         temperature = val * 0.125
#     oled.fill(0)
#     oled.text("Temp:" + str(temperature) + "C", 0, 0)
#     oled.show()
#     time.sleep(3)
#     print("Temp:", temperature)
