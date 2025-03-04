"""
This module is used to connect the Raspberry Pi Pico to a WiFi network.
"""

import network
import time


class Wifi:
    def __init__(self: object, ssid: str, key: str):
        self.ssid = ssid
        self.key = key

    def connect(self):
        """
        Connects the Raspberry Pi Pico to the WiFi network.
        """
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(self.ssid, self.key)
            attempt = 0
            while not sta_if.isconnected() and attempt < 10:
                print('Attempt', attempt + 1)
                attempt += 1
                time.sleep(1)
            if not sta_if.isconnected():
                print('Failed to connect to network')
                return False
        print('network config:', sta_if.ifconfig())
        return True