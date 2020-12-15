def containsNumber(list, number):
    for i in range(0,len(list)):
        for j in range(i,len(list)):
            if list[i] + list[j] == number:
                return True
    return False

file = open('input.txt', 'r') 
lines = [int(line) for line in file.readlines()]
file.close()

outlyer = 0
preambleLength = 25
solution1 = 0
solution2 = 0

for i in range(preambleLength, len(lines)):
    preamble = lines[i-preambleLength:i]
    if not containsNumber(preamble, lines[i]):
        solution1 = lines[i]

for i in range(0, len(lines)):
    listsum = lines[i]
    j = i
    while listsum < solution1:
        j+=1
        listsum+=lines[j]
        if listsum == solution1:
            solution2 = min(lines[i:j+1])+max(lines[i:j+1])
print(solution2)