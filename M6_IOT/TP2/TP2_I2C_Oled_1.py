from machine import Pin, SoftI2C
import time
import ssd1306

#configuration du bus I2C sur l'ESP8266.
#le timeout est nécessaire pour eviter l'erreur watch dog si pas de réponse sur le Bus.

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text('Hello, World !', 0, 0)
oled.text('Hello World', 8, 7)
oled.text('Hello World', 56, 16)
oled.text('Hello World', 20, 30)
oled.text('Hello World', 121, 40)
oled.text('ABCDEFGHIJKLMNOP', 30, 57)
oled.show()