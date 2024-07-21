testArray = ["a", "a", "a", "b", "c"]

def _Check_three_and_two(arr):
    A = B = C = 0
    retn = False
    for x in arr:
        if x == "a":
            A += 1
        elif x == "b":
            B += 1
        else:
            C += 1
    else:
        if A or B or C >= 3 and A or B or C >= 2:
            retn = True

    return retn

print(_Check_three_and_two(testArray))