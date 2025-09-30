import paho.mqtt.client as mqtt
import time

broker = "172.20.10.11"
port = 1883
ping = "pjariwal/ping"
pong = "pjariwal/pong"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"connected to rpi")
    client.subscribe(ping)

def on_message_from_ping(client, userdata, message):
    number_received = int(message.payload.decode())
    print(f"Received: {number_received}")

    number_received += 1
    time.sleep(1)
    client.publish(pong, str(number_received))
    print(f"Published response: {number_received}")

def on_message_from_sub(client, userdata, message):
    number_received = int(message.payload.decode())
    print(f"Received: {number_received}")

    number_received += 1
    time.sleep(1)
    client.publish(ping, str(number_received))
    print(f"Published response: {number_received}")


client.on_connect = on_connect
client.message_callback_add(ping, on_message_from_ping)
client.message_callback_add(pong, on_message_from_sub)


if __name__ == "__main__":
    client.connect(broker, port, keepalive = 60)
    client.loop_forever()