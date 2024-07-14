import random

userInput = int(input("Enter a number: "))
arr = []

def _arrayIntializer(lengthOfArray):
    counter = 0
    while counter < lengthOfArray:
        arr.insert(counter, random.randint(1,10))
        counter += 1
    return arr

#print(_arrayIntializer(userInput))

def _sockMerchant(lenofArr, Arr): 
    numToreturn = 0
    for x in Arr:
        ocurrance = 0
        for y in Arr:
            if x == y:
                ocurrance += 1
        if ocurrance >= 2:
            numToreturn += int(ocurrance / 2)
    return numToreturn

print(f"\nThere are {_sockMerchant(userInput, _arrayIntializer(userInput))} pairs of socks in the pile\n")
        