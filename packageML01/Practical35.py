def show(*arr):
    print("No. of elements in arr = ",len(arr))
    print("Data types of arr = ", type(arr))
    print(arr)

show(1,2,3,4,5)
print("\n")

list1 = [1,2,3,4,5]
show(list1)

print()
show(*list1)

print()

tuple1 = (1,2,3,4,5)
show(tuple1)
show(*tuple1)