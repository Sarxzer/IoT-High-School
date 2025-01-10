from machine import Pin, Timer
import time

def blink(led):
    led.value(not led.value())

ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)
compteur = 0
ledR.off()
ledG.off()
ledB.off()
blinkTimer= Timer(-1)
blinkTimer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:blink(ledG))

while True:
    compteur=compteur+8
    print (compteur)
    time.sleep(2.5)
