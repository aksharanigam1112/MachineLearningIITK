# file ModuleTwo.py
import Module1 #this will make the wholw program of ModuleOne executed except the code of def()

print("Top-level in ModuleTwo.py")
print("ModuleTwo:__name__=",__name__)
Module1.func()
if __name__=="__main__":#name variable is available in every file it is hidden6
    print("ModuleOne.py is being run directly")#the file havinf name=main is always execued 1st.it acts as a main function from where the
    #main function is executed.(starting point)
else:
    print("ModuleOne.py is being imported into another module")
