import time
import board
import digitalio
import mcp3008

PIN = board.D5


led = digitalio.DigitalInOut(PIN)
led.direction = digitalio.Direction.OUTPUT
threshold = 600

led_on_duration = 0.1

led_is_on = False 

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False 
    time.sleep(0.5)



    #sound sensor
    led_on_until = 0
    adc = mcp3008.MCP3008()
    for i in range(0, 50):
        sound_level = adc.read([mcp3008.CH1])

        if sound_level > threshold: 
            led_on_until = time.time() + led_on_duration

        if time.time() < led_on_until:
            led.value = True
        else: 
            led.value = False

        
        
        time.sleep(0.1)

    adc.close()

