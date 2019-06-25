#First Method
f = open("sensor.txt","r")
f.close() # Close is necessary in this case

#Second Method in this case close is not required
with open("sensor.txt","r") as f:
    for line in f:
        print(line)
# File is auto-closable in this case