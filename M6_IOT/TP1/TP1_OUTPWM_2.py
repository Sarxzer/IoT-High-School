from machine import Pin, PWM
import time

ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)
buttonPin = Pin(19, Pin.IN)

duty_step= 125
ledG_pwm = PWM(ledG)
ledG_pwm.freq(10000)

interupt = 0
compteur = 0
sec = 0

def detectbutton(pin):
    global interupt
    interupt += 1
    if interupt == 0:
        ledG_pwm.duty_u16(65536)
    elif interupt == 1:
        ledG_pwm.duty_u16(int(65536*75/100))
    elif interupt == 2:
        ledG_pwm.duty_u16(int(65536*50/100))
    elif interupt == 3:
        ledG_pwm.duty_u16(int(65536*25/100))
    else:
        ledG_pwm.duty_u16(0)
        interupt = 0
    print("Interruption par le bouton")
    

buttonPin.irq(trigger=Pin.IRQ_FALLING, handler=detectbutton)



while True:
    compteur += 1
    print(compteur)
    time.sleep(4)