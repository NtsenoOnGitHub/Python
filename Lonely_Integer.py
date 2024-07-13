#https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

arr = [1,2,3,5,3,2,1]

def _lonelyInteger(arr):
    lonelyInteger = 0
    for x in arr:
        numToCheck = x
        occurance = 0

        for y in arr:
            if numToCheck == y:
                occurance += 1
            else:
                pass

        if occurance == 2:
            pass
        else:
            lonelyInteger = x

    return lonelyInteger


print(_lonelyInteger(arr))

