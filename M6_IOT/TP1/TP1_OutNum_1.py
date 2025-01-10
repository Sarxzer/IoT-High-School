from machine import Pin
import time
ledR = Pin(2, Pin.OUT)
while True:
    ledR.on()
    time.sleep(1)
    ledR.off()
    time.sleep(2)