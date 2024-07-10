
print("Exercise 1\n")

def DisplayMyDetails():
    print("Welcome")

DisplayMyDetails()

print("\nExercise 2\n")

def DisplayEvenNumbers():
    evenNumber = 2
    while evenNumber <= 20:
        print(evenNumber)
        evenNumber += 2

DisplayEvenNumbers()

print("\nExercise 3\n")

def DisplaySomeDetails(name):
    print("welocome", name)

DisplaySomeDetails("Ntseno")

print("\nExercise 4\n")

def CheckIfEven(number):
    if number % 2 == 0:
        print("The Number you Entered is even number")
    else:
        print("The Number you Entered is an odd number")
        
    print("The number you entered is an even number") if number % 2 == 0 else print("The number you enterd is an odd number")

userNumber = int(input("Enter a Number: "))
CheckIfEven(userNumber)
userNumber = int(input("Enter a Number: "))
CheckIfEven(userNumber)

print("\nExercise 5\n")

def SumNumbers(num1, num2):
    print(f"The sum of the two numbers is {num1+num2}")

SumNumbers(2,5)

print("\nExercise 6\n")

def rSumNumbers(num1, num2):
    return num1 + num2

print(f"The sum of 5 and 7 is {rSumNumbers(5,7)}")
print(f"The sum of 10 and 9 is {rSumNumbers(10,9)}")

print("\nExercise 7\n")

def rCheckEven(number):
    rtnValue = False
    if number % 2 == 0:
        rtnValue = True
    else:
        rtnValue = False
    return rtnValue

print(rCheckEven(3))
print(rCheckEven(4))

print("\nExercise 8a\n")

numbersArray = [44,76,55,33,67,85,90,36,77,50]

def aDisplayNumbers(numberArray):
    for x in numberArray:
        print(x)

aDisplayNumbers(numbersArray)


print("\nExercise 8b\n")

def aSumNumbers(numberArray):
    sum = 0
    for x in numberArray:
        sum += x
    return sum

print(f"The sum of the numbers in the supplied array is {aSumNumbers(numbersArray)}")





