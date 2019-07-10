import time
import datetime

startTime = offstarttime=datetime.time(21,0,0) # sunset time
offendtime=datetime.time(10,0,0) # sunrise time

onTime = 5000

while True:
    currentTime = datetime.datetime.now().time()
    if currentTime.hour >= 1 and datetime.datetime.now().time() < startTime:
        print("a")
        onTime = 600
    else:
        print(currentTime.hour)
        print("b")
        oneTime = 5000

#time on -done
#implement on/off time - do next