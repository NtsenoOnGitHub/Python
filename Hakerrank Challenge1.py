# Hakerrank Challenge1
#Task
#Given an integer, X , perform the following conditional actions:
#If X is odd, print Weird
#If X is even and in the inclusive range of 2 to 5, print Not Weird
#If X is even and in the inclusive range of 6 to 20, print Weird
#If X is even and greater than 20, print Not Weird
#Input Format
#A single line containing a positive integer, .
#Constraints
#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird

userNumber = int(input("Please Enter a number: ").strip())

if userNumber % 2 != 0: 
    print("Weird\n")
elif userNumber % 2 == 0 and (userNumber >= 2 and userNumber <= 5):
    print("Not Weird\n")
elif userNumber % 2 == 0 and (userNumber >= 6 and userNumber <= 20):
    print(" Weird\n")
else:
    print("Not Weird\n")

