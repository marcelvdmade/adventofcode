file = open('input.txt', 'r') 
lines = file.readlines()
file.close()

xMax = len(lines[0])-1 #mod 31
yMax = len(lines)    #lines[323] is eindpunt

trees1 = 0
trees2 = 0
trees3 = 0
trees4 = 0
trees5 = 0

#Right 1, down 1. 68
for y in range(0,yMax, 1):
    xIndex = (y * 1) % xMax
    if lines[y][xIndex:xIndex+1] == '#':
        trees1 +=1
#Right 3, down 1. 268
for y in range(0,yMax, 1):
    xIndex = (y * 3) % xMax
    if lines[y][xIndex:xIndex+1] == '#':
        trees2 +=1
#Right 5, down 1. 73
for y in range(0,yMax, 1):
    xIndex = (y * 5) % xMax
    if lines[y][xIndex:xIndex+1] == '#':
        trees3 +=1
#Right 7, down 1. 75
for y in range(0,yMax, 1):
    xIndex = (y * 7) % xMax
    if lines[y][xIndex:xIndex+1] == '#':
        trees4 +=1
#Right 1, down 2. 28
for y in range(0,yMax, 2):
    xIndex = int((y /2) % xMax)
    print(xIndex, y)
    if lines[y][xIndex:xIndex+1] == '#':
        trees5 +=1

print(trees1, trees2, trees3, trees4,trees5)
print(trees1 * trees2 * trees3 * trees4 * trees5)
