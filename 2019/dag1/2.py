import math

def getFuel(weight):
    fuelTotal = 0
    while weight > 0:
        fuel = math.floor(weight/3) - 2
        weight = fuel
        if fuel > 0:
            fuelTotal += fuel
    return fuelTotal

file = open('input.txt', 'r') 
moduleWeights = [int(line) for line in file.readlines()]
file.close()

totalFuel = 0

for weight in moduleWeights:
        totalFuel += getFuel(weight)

print(totalFuel)