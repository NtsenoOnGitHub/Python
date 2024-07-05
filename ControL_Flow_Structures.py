userInPut1 = float(input("Enter the first Number: ").strip())
userInput2 = float(input("Enter the second Number: ").strip())

def compareFunction(num1, num2):
    if num1 > num2: 
        comparison = f"{num1} is greater than {num2}"
    elif num1 < num2:
        comparison = f"{num1} is less than {num2}"
    else:
        comparison = f"{num1} is eqaul to {num2}"
    return comparison

print(f"\n{compareFunction(userInPut1, userInput2)}\n")

# Exercise 2
# Write an application that obtains
#two numbers from the user, and displays them, but rejects any input where
#both numbers are greater than 10 and asks for two new numbers.


numOne = int(input("Enter a number: ").strip())
numTwo = int(input("Enter a number: ").strip())

def logicFunction(number1, number2):
    while number1 and number2 > 10:
        number1 = int(input("Enter a number: ").strip())
        number2 = int(input("Enter a number: ").strip())
    print(f"Number one is {number1} and number two is {number2}")

logicFunction(numOne, numTwo)

