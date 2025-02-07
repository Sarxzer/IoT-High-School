import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "server-iot-VAILLENDET.local"
MQTT_TOPIC = "secu/publishPAHO"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER)
counter = 0
while counter<100:
    counter += 1
    client.publish(MQTT_TOPIC,"message_{}".format(counter))
    print("message_{}".format(counter))
    time.sleep(5)

client.disconnect()       