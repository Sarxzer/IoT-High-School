import network
import socket
import time

#parametres de l'AP
ssid="AP-IOT-BPCIEL"
key="wificielCIEL2024$"

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, key)
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

print("start programme")
if connect():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print('listening on', addr)

    def web_page():
        html = """<!DOCTYPE html>
                <html>
                <head>
                <title>Pico W</title>
                </head>
                <body style="background-color:powderblue;">
                <h1 style="color:blue;">Hello, World!</h1>
                <p style="font-family:courier;"> Ceci est la page du serveur
                web Pico Pi IoT</p>
                </body>
                </html>
                """
        return html

    while True:
        print("Attente d'une connexion client")
        connexionClient, adresse = s.accept()
        connexionClient.settimeout(4.0)
        print("Connecté avec le client", adresse)

        print("Attente requete du client")
        requete = connexionClient.recv(1024)    #requête du client
        requete = str(requete)
        print("Requete du client = ", requete)
        connexionClient.settimeout(None)

        print("Envoi reponse du serveur : code HTML a afficher")
        connexionClient.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        reponse = web_page()
        connexionClient.send(reponse)
        connexionClient.close()
        print("Connexion avec le client fermee")
else:
    print("Unable to start server due to network connection failure")