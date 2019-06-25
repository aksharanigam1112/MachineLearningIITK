
d = { 'A' : 'Java' , 'B' : 'J2ee' , 'C' : 'Android' , 'D' : 'Python' , 'E':'Hadoop' , 'Key' : 'Value' }

print("Dictionary = " , d)

d['B'] = 'India'
d['F'] = 'Japan'
print(d)
d['B'] = 'Chile'  #If same key value is used the value of the previous existing key gets changed it doesn't give erro
print(d)

# print(d.keys())
#
# print(d.__len__())
