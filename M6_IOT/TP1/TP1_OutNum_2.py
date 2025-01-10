from machine import Pin
import time
ledG = Pin(3, Pin.OUT)
while True:
    ledG.on()
    time.sleep(0.5)
    ledG.off()
    time.sleep(1.5)