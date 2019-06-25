import os
print("\nos.name = " , os.name)
print("\nos.getenv('PATH') = ",os.getenv('PATH'))
print("\nos.getcwd() =",os.getcwd() )

os.mkdir("AksharaNigam")
os.chdir("AksharaNigam")

print("\nos.getcwd() = ",os.getcwd())

os.chdir("..")
os.chdir("..")
os.chdir("packageML02")
os.mkdir("Songs")

print("\nos.getcwd()",os.getcwd())
# os.rmdir("Songs")
