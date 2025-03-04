from machine import SoftI2C, Pin
import ssd1306

class Oled:
    """
    Class to interact with the OLED display with a ssd1306 driver.
    """

    def __init__(self, scl: int, sda: int, width: int, height: int):
        """
        Constructor of the class.
        """
        self.i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda), freq=100000, timeout=5000)
        self.oled = ssd1306.SSD1306_I2C(width, height, self.i2c)
    
    def text(self, text: str, x: int, y: int):
        """
        Display text on the OLED display.
        """
        self.oled.text(text, x, y)
    
    def show(self):
        """
        Show the content of the OLED display.
        """
        self.oled.show()
    
    def fill(self, fill: int):
        """
        Fill the OLED display with a color.
        """
        self.oled.fill(fill)
        