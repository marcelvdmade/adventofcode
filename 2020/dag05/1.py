def getRow(letters, rowList):
    if len(letters) == 1:
        if letters[0] == "F":
            return int(rowList[0])
        return int(rowList[1])
    half = int(len(rowList)/2)
    if letters[0:1] == "F":
        return getRow(letters[1:], rowList[0:half])
    return getRow(letters[1:],rowList[half:])

def getColumn(letters, columnList):
    if len(letters) == 1:
        if letters[0] == "L":
            return int(columnList[0])
        return int(columnList[1])
    half = int(len(columnList)/2)
    if letters[0:1] == "L":
        return getColumn(letters[1:], columnList[0:half])
    return getColumn(letters[1:],columnList[half:])

file = open('input.txt', 'r') 
lines = file.readlines()
file.close()

rows = list(range(0,128))
columns = list(range(0,8))
maxId = 0

for line in lines:
    r = getRow(line[0:7], rows)
    c = getColumn(line[7:10], columns)
    id = (r * 8) + c
    if id > maxId:
        maxId = id

print(maxId)