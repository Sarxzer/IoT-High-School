# This is the main file of my firmware.
# It while display the temperature from the LM75a sensor on the OLED display. And host a web page to see the temeperature and turn on and off the LEDs.

from machine import Pin, I2C, Timer, PWM
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

# Initialize Web Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

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

# Initialize Web Page
def web_page(temperature):
    # HTML page with temperature and RGB LED control with sliders
    html = """<DOCTYPE html>
    <html> 
    <head>
        <title>Raspberry Pi Pico</title>
    </head>
    <body>
        <h1>Temperature: """ + str(temperature) + """</h1>
        <h2>LED</h2>
        <a href=\"/?led=on\"><button>LED ON</button></a>
        <a href=\"/?led=off\"><button>LED OFF</button></a>
        <h2 id="rgb">RGB LED</h2>
        <input type="range" min="0" max="255" value="0" class="slider" id="red">
        <input type="range" min="0" max="255" value="0" class="slider" id="green">
        <input type="range" min="0" max="255" value="0" class="slider" id="blue">
        <script>
            var sliders = document.querySelectorAll('.slider');
            var rgb = document.getElementById('rgb');
            sliders.forEach(function(slider) {
                slider.oninput = function() {
                    var red = document.getElementById('red').value;
                    var green = document.getElementById('green').value;
                    var blue = document.getElementById('blue').value;
                    rgb.style.color = 'rgb(' + red + ',' + green + ',' + blue + ')';
                    var xhr = new XMLHttpRequest();
                    xhr.open("GET", "/?red=" + red + "&green=" + green + "&blue=" + blue, true);
                    xhr.send();
                }
            });
        </script>        
    </body>
    </html>"""
    return html

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
    temperature = lm75a.read()
    # Host a web page  
    print("Attente d'une connexion client")
    connexionClient, adresse = s.accept()
    connexionClient.settimeout(4.0)
    print("Connecté avec le client", adresse)

    print("Attente requete du client")
    requete = connexionClient.recv(1024)    #requête du client
    requete = str(requete)
    print("Requete du client = ", requete)
    connexionClient.settimeout(None)

    # EXEMPLE DE REQUETE
    #'GET /?red=169&green=0&blue=0 HTTP/1.1\r\nHost: 192.168.1.38\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0\r\nAccept: */*\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.38/?led=on\r\nPriority: u=0\r\n\r\n'
    # Get the LED state
    if requete.find('/?led=on') == 6:
        print("LED ON")
        led_color(255, 255, 255)
    elif requete.find('/?led=off') == 6:
        print("LED OFF")
        led_color(0, 0, 0)
    
    # Get the RGB LED state
    if requete.find('/?red=') == 6:
        red = int(requete[requete.find('/?red=')+6:requete.find('&green=')])
        green = int(requete[requete.find('&green=')+7:requete.find('&blue=')])
        blue = int(requete[requete.find('&blue=')+6:requete.find('HTTP')-1])
        print("RGB LED: red=", red, " green=", green, " blue=", blue)
        led_color(red, green, blue)

    print("Envoi reponse du serveur : code HTML a afficher")
    connexionClient.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    reponse = web_page(temperature)
    connexionClient.send(reponse)
    connexionClient.close()
    print("Connexion avec le client fermee")