# This is the main file of my firmware.
# It while display the temperature from the LM75a sensor on the OLED display. And host a web page to see the temeperature and turn on and off the LEDs.

from machine import Pin, I2C, Timer, PWM
import time
import ujson

from libs.wifi import Wifi
from libs.lm75a import lm75a
from libs.oled import Oled

# Get configuration from config.json
with open('config.json') as f:
    config = ujson.load(f)

# Initialize OLED display
oled = Oled(config['i2c']['scl'], config['i2c']['sda'], config['Oled']['Width'], config['Oled']['Height'])

# Connect to WiFi
oled.text("Connecting to ", 0, 0)
oled.text("Wifi :", 0, 10)
oled.text(config['Wifi']['ssid'], 0, 20)
oled.show()
wifi = Wifi(config['Wifi']['ssid'], config['Wifi']['key'])
wifi.connect()
oled.text("Connected to ", 0, 0)
oled.text("Wifi !", 0, 10)
oled.show()

# Initialize LM75a sensor
lm75a = lm75a(20, 21)

# RGB LED (Pin 2, 3, 4)
led_red = Pin(2, Pin.OUT)
led_green = Pin(3, Pin.OUT)
led_blue = Pin(4, Pin.OUT)
led_red_pwm = PWM(led_red)
led_red_pwm.freq(1000)
led_green_pwm = PWM(led_green)
led_green_pwm.freq(1000)
led_blue_pwm = PWM(led_blue)
led_blue_pwm.freq(1000)

# Button (Pin 19)
button = Pin(19, Pin.IN)

# RGB LED control (0-255)
def led_color(red, green, blue):
    led_red_pwm.duty_u16((65535*red)//255)
    led_green_pwm.duty_u16((65535*green)//255)
    led_blue_pwm.duty_u16((65535*blue)//255)

led_color(0, 0, 0)

def refreshOled(pin):
    print("Button pressed")
    # Display temperature on OLED
    oled.fill(0)
    temperature = lm75a.read()
    oled.text("Temperature:", 0, 0)
    oled.text(str(temperature), 0, 10)
    oled.show()
    time.sleep(5)
    oled.fill(0)
    oled.show()

button.irq(trigger=Pin.IRQ_FALLING, handler=refreshOled)

while True:
    pass