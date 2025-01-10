from machine import Pin
from time import sleep

ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)
buttonPin = Pin(19, Pin.IN)

compteur = 0
ledR.off()
ledG.off()
ledB.off()

def detectbutton(pin):
    print("Interruption par le bouton")
    ledG.on()
    sleep(1)
    ledG.off()

buttonPin.irq(trigger=Pin.IRQ_FALLING, handler=detectbutton)

while True:
    compteur = compteur +1
    print(compteur)
    sleep(0.5)