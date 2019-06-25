fob = open("sensor.txt","r")
x  = fob.readlines()
print(x[len(x)-1])

print( x[-1])
fob.close()

