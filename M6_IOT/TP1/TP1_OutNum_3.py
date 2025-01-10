from machine import Pin
import time

ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)

while True:
    ledG.on()
    time.sleep(1)
    ledG.off()
    ledR.on()
    time.sleep(2)
    ledR.off()