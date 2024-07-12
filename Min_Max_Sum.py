# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

import random

arrSize = int(input("Enter a number: ").strip())

# 
def _ArrayMethod(arrLen):
    counter = 0
    arr = []
    while counter < arrLen:
        arr.insert(counter, random.randint(1, 10))
        counter += 1
    arr.sort()
    maxSum = 0
    minSum = 0
    for x in arr:
        maxSum += x
    maxSum -= arr[arrLen-1]
    #print(arr)
    arr.sort(reverse=True)
    for x in arr:
        minSum += x
    minSum -= arr[arrLen-1]
    print(arr)
    return f"The max sum of the the numbers is {maxSum}\nThe min sum of the numbers is {minSum}"

print(_ArrayMethod(arrSize))