# ModuleOne.py
print("top-level in ModuleOne.py")
print("Module One:__name__=",__name__)
def func():
    print("func() in ModuleOne.py")

if __name__=="__main__":
    print("ModuleOne.py is being run directly")
else:
    print("ModuleOne.py is being imported into another module")
