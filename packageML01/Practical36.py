def show(name="N" , phone ="P" , city="C"):
    print("Name = ",name)
    print("Phone = ",phone)
    print("City = ",city)
    return

show(name="India" , phone = "1111" , city = "Noida")
print("\n")
dict1 = { 'name' : "India" , 'phone' : "1111" , 'city' : 'Noida'}
show(dict1)
print("\n")
show(*dict1)
print("\n")
show(**dict1)