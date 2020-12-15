import math

file = open('input.txt', 'r') 
moduleWeights = [int(line) for line in file.readlines()]
file.close()

totalFuel = 0

for weight in moduleWeights:
    totalFuel += int(math.floor(weight/3) -2)

print(totalFuel)