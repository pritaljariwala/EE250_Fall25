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

# clear lcd screen  before starting main 
setText("")
timer = 0
previous_reading = 0
previous_thresh = 0
while True:
  try:
    # Read distance value from Ultrasonic
    ultrasonic_reading = grovepi.ultrasonicRead(ultrasonic_ranger)
    threshold = grovepi.analogRead(potentiometer)/10

    if ultrasonic_reading < threshold:
      obj_present = "OBJ PRES"
    else:
      obj_present = ""
  
  except Exception as e:
    print ("Error:{}".format(e))
  time.sleep(0.1)

    
  # TODO: format LCD text according to threshhold
  if (previous_thresh < threshold or previous_reading != ultrasonic_reading):
        setText(str(ultrasonic_reading) + "\n" + str(threshold) + " " + obj_present)
        previous_threshold = threshold
        previous_reading = ultrasonic_reading
  elif (previous_thresh != threshold or ultrasonic_reading != previous_reading):
        setText(str(ultrasonic_reading) + "\n" + str(threshold) + " ")
        previous_threshold = threshold
        previous_reading = ultrasonic_reading
  else:
        timer = timer + 1








