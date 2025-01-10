from machine import Pin
import time

buttonPin = Pin(19, Pin.IN)
ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)

buttonState = 0

while True:
    buttonState = buttonPin.value()
    
    if buttonState == 1:
        ledG.on()
        ledR.off()
    else:
        ledR.on()
        ledG.off()