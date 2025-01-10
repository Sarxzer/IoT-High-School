from machine import Pin
import time
buttonPin = Pin(19, Pin.IN)
buttonState = 0
while True:
    buttonState = buttonPin.value()
    print(buttonState)
    if buttonState == 0:
        print("bouton relaché")
    else :
        print("bouton appuyé")
    time.sleep(0.500)