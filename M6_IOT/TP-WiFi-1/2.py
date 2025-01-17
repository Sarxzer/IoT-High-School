import network
import socket

ssid= "AP-VAILLENDET"
cle= "secusnVAILLENDET$1234*"

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid,password=cle)
ap.config(pm=0xa11140)  #désactiver le mode power-save
ap.active(True)

while ap.active== False: pass

print("Access Point actif")
print(ap.ifconfig())
print("Réseau wifi: ", ssid, "password: ", cle)

def web_page():
    html = """
    <!DOCTYPE html>
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

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)
print('listening on', addr)

while True:
    print("Attente d'une connexion client")
    connexionClient, adresse = s.accept()
    connexionClient.settimeout(4.0)
    print("Connecté avec le client", adresse)

    print("Attente requete du client")
    requete = connexionClient.recv(1024)
    requete = str(requete)
    print("Requete du client = ", requete)
    connexionClient.settimeout(None) #requête du client

    print("Envoi reponse du serveur : code HTML a afficher")
    connexionClient.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    reponse = web_page()
    connexionClient.send(reponse)
    connexionClient.close()
    print("Connexion avec le client fermee")