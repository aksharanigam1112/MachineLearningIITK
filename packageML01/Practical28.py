def group1():
    a = int(input("\nEnter 1st no:-"))
    b =  int(input("\nEnter 2nd no :-"))
    c = a+b
    print("\nAddition result = ",c)
    return

def group2(x,y):
    c = x+y
    print("\nAddition Result = ",c)
    return

def group3(x,y):
    c = x+y
    return c

group1()
print("="*20)
group1()

a = int(input("\nEnter 1st no:-"))
b =  int(input("\nEnter 2nd no :-"))

group2(a,b) #Calling function

print("\nAddition Result = ", group3(a,b))