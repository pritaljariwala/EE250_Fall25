# Prital Jariwala
# Lucas Greer
# https://github.com/pritaljariwala/EE250_Fall25/tree/main

import paho.mqtt.client as mqtt
import time

broker = "172.20.10.11"
port = 1883
initial_send = 0

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected to rpi")
    publish_ping(initial_send)

def publish_ping(number):
    number_to_send = str(number)
    client.publish("pjariwal/ping", number_to_send)
    print(f"Published to pjariwal/ping: {number_to_send}")

def start_publishing():
    current_number = initial_send
    while True: 
        publish_ping(current_number)
        current_number += 1
        time.sleep(1)

if __name__ == "__main__" : 
    client.on_connect = on_connect

    client.connect(broker, port, keepalive=60)

    client.loop_start()

    start_publishing()