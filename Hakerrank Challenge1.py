
# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

userNumber = int(input("Please Enter a number: ").strip())

if userNumber % 2 != 0: 
    print("Weird\n")
elif userNumber % 2 == 0 and (userNumber >= 2 and userNumber <= 5):
    print("Not Weird\n")
elif userNumber % 2 == 0 and (userNumber >= 6 and userNumber <= 20):
    print(" Weird\n")
else:
    print("Not Weird\n")

