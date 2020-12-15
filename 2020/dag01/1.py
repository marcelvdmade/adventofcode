file = open('input.txt', 'r') 
intLines = [int(line) for line in file.readlines()]
file.close()

for i in range(0,len(intLines)):
    for j in range(i,len(intLines)):
        if intLines[i] + intLines[j] == 2020:
            print(intLines[i]*intLines[j])