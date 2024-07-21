def high_and_low(numbers):
    small = 0
    high = 0
    
    for x in numbers:
        if x != ' ':
            small = int(x)
            high = int(x)

            for y in numbers:
                if y != ' ':
                    cast = int(y)
                    if cast < small:
                        small = cast
                    if cast > high:
                        high = cast
        else:
            continue
    
    return f'{high} {small}'

print(high_and_low("1 2 -3 4 5"))