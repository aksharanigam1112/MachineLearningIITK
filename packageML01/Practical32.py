def sum(*values):
    sum = 0
    for num in values:
        sum+=num
    print("Addition result of %d numbers %d" %(len(values) , sum ))
    return

sum(2,3,4,5)
sum(3,4,6)