import os
import time
import paho.mqtt.client as mqtt
from utils.constants import Constants

class MQTTService:
    _client = []

    def __init__(self):
        self._client = mqtt.Client()

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT")
        else:
            print("Failed to connect to MQTT")

    def _on_disconnect(self, client, userdata, rc):
        self._reconnect()

    def _reconnect(self):
        print('Failed to connect to MQTT Broker. Reconnecting...')
        time.sleep(5)
        self.connect()

    def connect(self):
        self._client.on_connect = self._on_connect
        self._client.on_disconnect= self._on_disconnect
        self._client.connect(os.environ['MQTT_SERVER'])

    def send(self, topic, message):
        self._client.publish(topic, message, qos=0, retain=False)
