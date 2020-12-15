file = open('input.txt', 'r') 
lines = file.readlines()
file.close()

xTravel = 3
yTravel = 1

xMax = len(lines[0])-1 #mod 31
yMax = len(lines)    #lines[323] is eindpunt

trees = 0

for y in range(0,yMax), yTravel:
    xIndex = (y * xTravel) % xMax
    if lines[y][xIndex:xIndex+1] == '#':
        trees +=1

print(trees)