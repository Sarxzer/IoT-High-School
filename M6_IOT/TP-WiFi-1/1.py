import network
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