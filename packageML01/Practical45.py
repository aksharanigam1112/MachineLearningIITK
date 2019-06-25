file = open("lines.txt","w")
for i in range(1,1112):
    file.write("{0:04d} This is developed @iitk\n".format(i))
file.close()