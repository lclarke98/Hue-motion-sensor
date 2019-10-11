
while True:
    currentTime = datetime.datetime.now().time()
    if currentTime.hour >= 1 and datetime.datetime.now().time() < startTime:
        print("a")
        onTime = 600
    else:
        print(currentTime.hour)
        print("b")
        onTime = 5000