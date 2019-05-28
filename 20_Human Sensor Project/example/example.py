from microbit import *

sensor = pin1
eyes = pin0
bell = pin2

def allOff():
    eyes.write_digital(0)
    bell.write_digital(0)
   
def allOn():
    eyes.write_digital(1)
    bell.write_digital(1)
   
def eyesBlink():
    eyes.write_digital(1)
    bell.write_digital(0)
    sleep(500)
    eyes.write_digital(0)
    sleep(500)
   
def allBlink():
    eyes.write_digital(1)
    bell.write_digital(1)
    sleep(500)
    eyes.write_digital(0)
    bell.write_digital(0)
    sleep(500)
   
def heart():
    newImage = Image("09090:"
                     "99999:"
                     "99999:"
                     "09990:"
                     "00900")
    display.show(newImage)
   
def noHeart():
    newImage = Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "00000")
    display.show(newImage)


while True:
    sensorValue = sensor.read_analog()
    print(sensorValue)
    sleep(100)
   
    if (sensorValue > 200):
        allOff()
        noHeart()
    if (sensorValue >= 100 and sensorValue < 200):
        eyesBlink()
        noHeart()
    if (sensorValue >=50 and sensorValue < 100):
        allBlink()
    if (sensorValue < 50):
        allOn()
	heart()
