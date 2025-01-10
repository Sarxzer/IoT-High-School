from machine import Pin, PWM
import time

duty_step= 125
ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)
ledR.off()
ledG.off()
ledB.off()
ledR_pwm = PWM(ledR)
ledR_pwm.freq(10000)

while True:
    ledR_pwm.duty_u16(65536)
    time.sleep(1)
    ledR_pwm.duty_u16(int(65536/2))
    time.sleep(1)
    ledR_pwm.duty_u16(int(65536/3))
    time.sleep(1)
    ledR_pwm.duty_u16(int(65536/4))
    time.sleep(1)
    ledR_pwm.duty_u16(0)
    time.sleep(1)
    # Increase the duty cycle gradually
    for duty_cycle in range(0, 65536, duty_step):
        ledR_pwm.duty_u16(duty_cycle)
        time.sleep(0.005)
        # Decrease the duty cycle gradually
    for duty_cycle in range(65536, 0, -duty_step):
        ledR_pwm.duty_u16(duty_cycle)
        time.sleep(0.005)
