userInPut1 = float(input("Enter the first Number: ").strip())
userInput2 = float(input("Enter the second value: ").strip())

comparison = f"{userInPut1} is eqaul to {userInput2}"

if userInPut1 > userInPut1: 
    comparison = f"{userInPut1} is greater than {userInput2}"
elif userInPut1 < userInput2:
    comparison = f"{userInPut1} is less than {userInput2}"
else:
    comparison = f"{userInPut1} is eqaul to {userInput2}"

print(comparison)

