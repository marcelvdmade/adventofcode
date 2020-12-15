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

for i in range(preambleLength, len(lines)):
    preamble = lines[i-preambleLength:i]
    if not containsNumber(preamble, lines[i]):
        print(lines[i])
