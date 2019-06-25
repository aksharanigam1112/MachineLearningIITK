import shelve
products = shelve.open("MyProduct.txt")
products['P001'] = "Mouse"
products['P002'] = "Keyboard"
products['P003'] = "Monitor"
products['P004'] = "Printer"
products['P005'] = "DVD"
products['P003'] = "Music System"

products.close()
print("All Products data saved in our shelve")