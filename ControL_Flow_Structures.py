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

