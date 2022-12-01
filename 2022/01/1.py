file = open('input.txt', 'r') 
fileContent = file.read()
file.close()

lines = fileContent.splitlines()
sums = [0]

def calculateSums():
    counter = 0;
    for i in range(0,len(lines)):
        if lines[i] == "":
            sums.append(0)
            counter += 1
        else:
            sums[counter] += int( lines[i])

def findMaxValuesTop(topAmount):
    result = 0
    while topAmount >= 1:
        maxResult = max(sums)
        result += maxResult
        sums.remove(maxResult)
        topAmount -= 1
    return result


calculateSums()
#print(findMaxValuesTop(1)) #67450
print(findMaxValuesTop(3)) #
