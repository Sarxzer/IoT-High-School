from machine import Pin
import time

ledR = Pin(2, Pin.OUT)
ledG = Pin(3, Pin.OUT)
ledB = Pin(4, Pin.OUT)

def color(R,G,B):
    ledR.value(R)
    ledG.value(G)
    ledB.value(B)

while True:
    color(255,0,0)
    time.sleep(2)
    color(0,255,0)
    time.sleep(2)
    color(0,0,255)
    time.sleep(2)
    color(255,255,0)
    time.sleep(2)
    color(0,255,255)
    time.sleep(2)
    color(255,0,255)
    time.sleep(2)
    color(255,255,255)
    time.sleep(2)
    color(0,0,0)
    time.sleep(1)