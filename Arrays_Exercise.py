
print("Exercise 1\n")
dataArray = [3,7,5,2,3,9,10,2,1,8]

for x in dataArray:
    print(x)

print("\nExercise 2")

sumofNumbers = 0

for x in dataArray:
    sumofNumbers = sumofNumbers + x

print(sumofNumbers)

print("\nExercise 3")

productOfTen = 0
indexVar = 0

for x in dataArray:
    productOfTen = x*10
    dataArray[indexVar] = productOfTen
    indexVar = indexVar + 1

for x in dataArray:
    print(x)

print("\nExercise 4")
print("\nExercise 5\n")

userNumbers = []

num1 = int(input("Enter a number: "))
userNumbers.append(num1)
num2 = int(input("Enter a number: "))
userNumbers.append(num2)
num3 = int(input("Enter a number: "))
userNumbers.append(num3)
num4 = int(input("Enter a number: "))
userNumbers.append(num4)
num5 = int(input("Enter a number: "))
userNumbers.append(num5)

for x in userNumbers:
    print(x)

print("\nExercise 9")

mark = [56, 33, 57, 88, 66, 44, 70, 30, 50, 97]
sumVar = 0.0

for x in mark:
    sumVar = sumVar + x

average = sumVar/len(mark)
print(average)
# comment


