import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

grovepi.lcdInit()

# clear lcd screen  before starting main loop
grovepi.setText("")


# TODO:read distance value from Ultrasonic Ranger and print distance on LCD
while True:
  try:
    # Read distance value from Ultrasonic
    ultrasonic_reading = grovepi.ultrasonicRead(ultrasonic_ranger)
    threshold = grovepi.analogRead(potentiometer)
    print(f"Distance: {ultrasonic_reading}")

    if ultrasonic_reading < threshold:
      obj_present = "OBJ PRES"
    else:
      obj_present = ""
  
  except Exception as e:
    print ("Error:{}".format(e))
  time.sleep(0.1)
        
    
  # TODO: format LCD text according to threshhold
  grovepi.setText()
  except IOError:
    print("Error")