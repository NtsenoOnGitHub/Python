userChoice = ""
userValue = 0
breaker = False

def ToCel(tempValue):
    return (tempValue - 32)/1.8

def ToFah(temValue):
    return temValue*1.8 + 32

def ToKel(temValue):
    return temValue + 273.15

def ToRank(tempValue):
    return(tempValue + 273.15) * 1.8

def DisplayMenu():
    print("\nCelsius Converter")
    print("=============================")
    print("C - Celsius to Fahrenheit")
    print("F - Fahrenheit to Celsius")
    print("K - Celsius to Kelvin")
    print("R - Celsius to Rankine")
    print("X - Exit")

def GetMenuOption():
    return str(input("\nPlease enter C, F, K, R or X: ")).strip()

def GetValue():
    return int(input("\nPlease enter a value to convert: "))

def printResults(fromValue, fromString, result, toString):
    print(f"\n{fromValue} {fromString} is {result} {toString}")

while userChoice != "X" or userChoice != "x":
    DisplayMenu()
    userChoice = GetMenuOption()
    if userChoice == "C" or userChoice == "c":
        userChoice = "Celsius"
        userValue = GetValue()
        printResults(userValue, userChoice, ToCel(userValue), "Fahrenheit")
    elif userChoice == "F" or userChoice == "f":
        userChoice = "F"
        userValue = GetValue()
        printResults(userValue, "Fahrenheit", ToCel(userValue), "Celsius")
    elif userChoice == "K" or userChoice == "k":
        userChoice = "K"
        userValue = GetValue()
        printResults(userValue, "Fahrenheit", ToCel(userValue), "Celsius")
    elif userChoice == "R" or userChoice == "r":
        userChoice = "R"
        userValue = GetValue()
        printResults(userValue, "Fahrenheit", ToCel(userValue), "Celsius")
    elif userChoice == "X" or userChoice == "x":
        userChoice = "X"
        print("\nThank you, Goodbey")
        break
    else:
        print("\nInvail option, Please try again \n")

    



    