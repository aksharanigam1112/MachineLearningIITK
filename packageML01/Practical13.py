arr= ['Mary','had','a','little','lamb']
print(enumerate(arr))
for i,j in enumerate(arr):
    print(i,"=",j)

print("\nBinding the index position with its' values is called Enumeration\n")

arr= [['Mary','had'],['a'],['little','lamb']]
for i,j in enumerate(arr):
    print(i,"=",j)