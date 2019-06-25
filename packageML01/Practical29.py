def show(empName , phn = "1234567890" , city = "Lucknow" , company = "XYZ" ):
    print("\nEmpName = ",empName,"phone = ", phn , "city = ",city,"company = ",company)

#Rule 1
show("Chintu")

#Rule 2
show("Chintu" , "999888")           #2 positional Arguments

#Rule 3
show(empName="Pappu" , phn ="877666")         #2 keyword Arguments
show(phn = "877666" , empName="Paps")
show(empName="Pappu" , city="Kanpur")

#Rule 4
show("Alisha" , "9898", city="Delhi")           #Mixed Mode


#Error code
#--------------------------------
# show()                                Required Argument missing
# show(empName="Akshara" , '999888')    non-keyword argument
# show("Akshara", empName="Alisha")     duplicate value
# show(name="Alisha")                   unknown keyword