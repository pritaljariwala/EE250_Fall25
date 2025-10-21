import time
import board
import digitalio

PIN = board.D5


led = digitalio.DigitalInOut(PIN)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False 
    time.sleep(0.5)
    