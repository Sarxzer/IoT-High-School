from machine import Pin, SoftI2C
import time
import ssd1306

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    for i in range(0,11):
        oled.fill(0)
        oled.text('COMPTE',48,4)
        oled.text('A REBOURS',36,13)
        oled.text(str(10-i),66,22)
        # cadre:
        oled.rect(16, 1, 112, 31, 1)
        oled.show()
        time.sleep(0.5)
        # texte déflant
    texte_complet = "Ce texte est beaucoup trop long pour cet ecran OLED"
    longueur = len(texte_complet)
    for n in range(0,longueur - 1):
        oled.fill(0)
        texte = texte_complet[n:16 + n]
        oled.text(texte,0,15)
        #lignes horizontales
        oled.hline(0,7,127,1)
        oled.hline(0,30,127,1)
        oled.show()
        time.sleep(0.15)
