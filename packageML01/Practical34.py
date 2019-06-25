def message(a,*args , **pairs):
    print("Value of a :-" , a)
    for num in args:
        print(num)
    print("\n")

    #1st method to print the dictionary

    for k in pairs:
        print(k,"=",pairs[k])
    print()

    #2nd method to print the dictionary

    mykeys = sorted(pairs.keys())
    for k in mykeys:
        print(k,":",pairs[k])
    return
message("A","B","C","D",name="Akshara",phone="9044651164",city="Lucknow")