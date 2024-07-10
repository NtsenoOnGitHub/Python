#The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# 123...n Where n represent an input from the user

n = int(input("Enter a number: "))
    
def _buildMethod(num):
    printString = ""
    counter = 1
    while counter <= num:
        printString += f"{counter}"
        counter += 1
    return printString
    
print(_buildMethod(n))
    
