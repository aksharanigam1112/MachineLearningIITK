
d = { 'A' : 'Java' ,  'C' : 'Android' , 'D' : 'Python' , 'E':'Hadoop' , 'Key' : 'Value' , 'B' : 'J2ee'}

print(d)

del d['E']
print("\nAfter deletion of 'E' = ",d)

print("d['B'] = ",d['B'])
# print("d[2] = " , d[2]) Dictionary does not support positional indexing
print("len(D) =  " , len(d))
print("'A' in d" , 'A' in d)
print("'a' in d" , 'a' in d)

print("d.keys() = " , d.keys())
print("sorted(d.keys()) = " , sorted(d.keys()))#Creates a list
print("d.values() = " , d.values()) #Creates a list
print("d.items() = ",d.items()) #Creates list of tuples

print("\n")

keylist = d.keys()
for k in sorted(keylist):
    print(k,d[k])

print("datatype =  ",type(d.items()))
for key , value in d.items():
    print(key,"=",value)

print("d['A'] = ", d['A'])
#print("d['Z'] = " , d['Z'])
print("d.get('Z') = ",d.get('Z'))