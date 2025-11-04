import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# === GPIO SETUP ===
GPIO.setmode(GPIO.BOARD)
LED_PIN = 11  # physical pin 11 for LED
GPIO.setup(LED_PIN, GPIO.OUT)
# === SPI + MCP3008 SETUP ===
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# === SENSOR CHANNELS ===
LIGHT_CH = 0  # channel 0 for light sensor
SOUND_CH = 1  # channel 1 for sound sensor

# === Thresholds (find these experimentally!) ===
LUX_THRESHOLD = 300  # adjust after testing
SOUND_THRESHOLD = 400  # adjust after testing

def blink_led(times, delay):
    """Blink the LED with given delay between on/off."""
    for _ in range(times):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    while True:
        # --- Step 1: Blink LED 5 times, 500ms on/off ---
        blink_led(5, 0.5)

        # --- Step 2: Light sensor test (5 seconds, every 100ms) ---
        print("\n=== LIGHT SENSOR TEST ===")
        start_time = time.time()
        while time.time() - start_time < 5:
            value = mcp.read_adc(LIGHT_CH)
            condition = "bright" if value > LUX_THRESHOLD else "dark"
            print(f"Light sensor value: {value} ({condition})")
            time.sleep(0.1)

        # --- Step 3: Blink LED 4 times, 200ms on/off ---
        blink_led(4, 0.2)

        # --- Step 4: Sound sensor test (5 seconds, every 100ms) ---
        print("\n=== SOUND SENSOR TEST ===")
        start_time = time.time()
        while time.time() - start_time < 5:
            value = mcp.read_adc(SOUND_CH)
            print(f"Sound sensor value: {value}")
            if value > SOUND_THRESHOLD:
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nDemo stopped by user.")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Goodbye 👋")
