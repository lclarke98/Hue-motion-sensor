import sys
sys.path.append("/home/pi/.local/lib/python2.7/site-packages")

from phue import Bridge
import RPi.GPIO as GPIO
import time
import datetime

# Connects pi to hue bridge
print( 'Waiting for network...')
time.sleep(30)
print ('Connected to network')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)
hueBridge=Bridge('192.168.1.7')
try:
        hueBridge.connect()
except ImportError:
        print ("Import error occurred!")
print ("Hue bridge connected")


#The next two lines define the time of day during which the pi should not turn on any lights even if motion is detected (for example: at bed time in a bedroom)
offstarttime=datetime.time(21,0,0) # sunset time
offendtime=datetime.time(10,0,0) # sunrise time

startTime = offstarttime=datetime.time(21,0,0)

while True:
    currentTime = datetime.datetime.now().time()
    if currentTime.hour >= 1 and datetime.datetime.now().time() < startTime:
        print("a")
        onTime = 600
    else:
        print(currentTime.hour)
        print("b")
        onTime = 5000

#after 1:30am change light time on length to 30sec

#Check if lights are already on
lightson=hueBridge.get_light(1, 'on')
if lightson: print( "Lights are already on.")

print ('Entering infinite loop...')
j=0
k=0
while True:
        i=GPIO.input(16) #Replace 16 with the actual GPIO pin where you connected your motion sensor
        timestamp=datetime.datetime.now().time()
        if (timestamp < offstarttime and timestamp > offendtime):
                if i==1:
                        j=j+1
                        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": Activity detected ", j, "time(s).")
                        if j==2:
                                print ("Lights will be on for 5 Minutes")
                                hueBridge.set_group(1, 'on', True) #Replace the number 1 with the light group number defined on Philips Hue. In my case Bedroom is 1.
                                lightson=True
                                j=0 
                                time.sleep(onTime) # Let the lights run at least 10 minutes (1500 seconds) once they are on
                        time.sleep(1)
                        k=0
                elif i==0:
                        if lightson==True:
                                k=k+1
                                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": No activity detected.")
                                if k==2:
                                        print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": Lights will go off")
                                        hueBridge.set_group(1, 'on', False) #Replace the number 1 with the light group number defined on Philips Hue. In my case Bedroom is 1.
                                        lightson=False
                                        k=0
                        else:
                                print ("Lights are already off. No command was sent.")
                        j=0
                        time.sleep(2) # Don't sleep too much if lights are off, keep looking for motion. Increasing this value makes the motion sensor respond slower.
        else:
                        time.sleep(60) # sleep a lot more during daytime/bedtime
