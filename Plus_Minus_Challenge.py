import random

arreSize = int(input("Enter the size of the array: ").strip())
loopCounter = 0
arr = []


while loopCounter < arreSize:
    num = random.randint(-100,100)
    arr.insert(loopCounter, num)
    loopCounter += 1

pos = 0
neg = 0
zer = 0

for x in arr:
    if x > 0:
        pos += 1
    elif x == 0:
        zer += 1
    else:
        neg += 1

posRatio = pos/arreSize
negRation = neg/arreSize
zerRatio = zer/arreSize
print(arr)
    
print(f"Positive ratio is {round(posRatio, 6)}\nthe Negetive ration is{round(negRation, 6)}\nthe ration of the number zero is {zerRatio}")


