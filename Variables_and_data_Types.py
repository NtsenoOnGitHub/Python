import random as randomNumber

xIsAnInt = 3 # xIsAnInt is of a type int
yIsAfloat = 5.0 # yIsAfloat is of a type float
zIsAstring = "I'm thee Z" # zIsAstring is of a type str
cIsAcomplex = 3j # cIsAcomplex is of a type complex
bIsAboolean = True # bIsAboolean is of type boolean
nIsAset = {"first", "Second", "Third"}
jIsAtuple = ("Fourth", "Fith", "Sixth")


#Printing to the console
print(str(xIsAnInt) + " is an Integer")
print(yIsAfloat, "is a float")
print(zIsAstring)
print(cIsAcomplex)
print(bIsAboolean, "\n")
print(nIsAset, "\n")
print(jIsAtuple, "\n")

#Getting input from the console
clientName = input("Please Type in your Name: ") 
clientIdNumber = int(input("Please Type in your ID Number: "))

#Printing the results from the user
print("The client's name is ",clientName)
print("The Client's ID Number is ", clientIdNumber)


