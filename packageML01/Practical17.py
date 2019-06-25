alpha = input("Enter alphabet to search : ")
for ch in "INDIA":
    if(ch==alpha):
        print(alpha,"found in the given word")
        break
else:
    print(alpha,"not found in the given word")