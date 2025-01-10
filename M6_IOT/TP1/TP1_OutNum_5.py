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
blinkTimer.init(period=500, mode=Timer.PERIODIC, callback=lambda t:blink(ledR))

while True:
    compteur=compteur+1
    print (compteur)
    time.sleep(2)