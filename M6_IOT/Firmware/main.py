# This is the main file of my firmware.
# It while display the temperature from the LM75a sensor on the OLED display. And host a web page to see the temeperature and turn on and off the LEDs.

from machine import Pin, I2C
import ssd1306
import time
import network
import socket
import ujson

from libs.wifi import Wifi
from libs.lm75a import lm75a
from libs.oled import Oled

# Get configuration from config.json
with open('config.json') as f:
    config = ujson.load(f)

# Connect to WiFi
wifi = Wifi(config['Wifi']['ssid'], config['Wifi']['key'])
wifi.connect()

# Initialize OLED display
oled = Oled(config['i2c']['scl'], config['i2c']['sda'], config['Oled']['Width'], config['Oled']['Height'])

# Initialize LM75a sensor
lm75a = lm75a(config['i2c']['scl'], config['i2c']['sda'])

while True:
    