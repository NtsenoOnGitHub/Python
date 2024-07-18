dataArray = [2,7,3,15]
target = 10

for x in dataArray:
    for y in dataArray:
        if x + y == target:
            result = f"{dataArray.index(x)} and {dataArray.index(y)}"
            
            
print(result)
            



    