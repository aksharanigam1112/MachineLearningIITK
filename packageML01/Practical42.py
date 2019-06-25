file = open("sensor.txt","r")
list1 = file.readlines()
print(list1[2])
list1[2] = "This is updated third line\n"
print(list1[2])
file.close()

fob = open("sensor.txt","w")
fob.writelines(list1)
fob.close()
