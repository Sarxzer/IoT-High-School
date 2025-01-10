from machine import Pin
import time

ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)

while True:
    ledR.on()
    time.sleep(2)
    ledR.off()
    ledG.on()
    time.sleep(2)
    ledG.off()
    ledB.on()
    time.sleep(2)
    ledB.off()
    time.sleep(1)
