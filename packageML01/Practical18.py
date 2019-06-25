num = int(input("Enter number for prime number test : "))

for i in range(2,num//2):
    if(num%i==0):
        print(num," is not a prime no. ")
        break
else:
    print(num," is a prime no. ")