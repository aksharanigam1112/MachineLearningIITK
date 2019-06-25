#Unpacking of Argument list

print( list( range(3,6)))

args = [3,6]
print(list(range(args[0] , args[1])))


print(list(range(*args)))