fob = open("sensor.txt","r")
print("\nData1 = ",fob.readline())
print("\nData2  =",fob.readlines())
fob.close()