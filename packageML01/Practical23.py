tu = ('Python','Java','J2ee','Android','Hadoop')
print("enumerate(tu) = ", enumerate(tu))

print("enumerate(tu) = " , tuple(enumerate(tu)))
print("enumerate(tu) = ", list(enumerate(tu)))

for k,v in enumerate(tu):
    print(k,"=",v)

for r in enumerate(tu):
    print(r)
