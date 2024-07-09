n = int(input("Enter a number: "))
    
def _buildMethod(num):
    printString = ""
    counter = 1
    while counter <= num:
        printString += f"{counter}"
        counter += 1
    return printString
    
print(_buildMethod(n))
    