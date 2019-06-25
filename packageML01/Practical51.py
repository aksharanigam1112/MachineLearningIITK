import shelve
products = shelve.open("MyProduct.txt")

for pid in products:
    print(pid, "=",products[pid])

print("All product details printed from file")