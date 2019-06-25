class Account:
    "Details for all Account"#documentation comment of class
    accCount=0   #Class variables-single copy existence

    def __init__(self,n,b) :  #Constructor-self start
        #the no. of time code is loaded it will run wid all other function

        self.name=n#instance variable(self.name)=local variable(n)
        self.balance=b#instance variable-(multi copy existance)any variable made wid extention as( self.variablename)
        Account.accCount=Account.accCount+1
        print("Constructor is working.",b)
    def displayCount(self):
        print("Total Account %d"%Account.accCount)

    def displayAccont(self):
        print("Name:",self.name,",Balance:",self.balance)

#Creatinh Instance Objects

ptr1=Account("Pappu",2000)#this loads the class Account in wid all other functions inside
ptr2=Account("Munni",5000)
#Accessing Attributes
print(ptr1.name)#this provide access