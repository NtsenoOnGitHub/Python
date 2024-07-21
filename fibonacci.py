def high_and_low(numbers):
    small = 0
    high = 0
    
    for x in numbers:
        if x == " ":
            numbers.pop(" ")
    
    for x in numbers:
        small = int(x)
        high = int(x)
        for y in numbers:
            if int(y) < small:
                small = y
            if int(y) > high:
                high = y
    
    return str(high + " " + small)

    print(high_and_low("1 2 3 4 5"))