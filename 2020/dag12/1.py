file = open('input.txt', 'r')
lines = file.readlines()
file.close()

grid = {'N':0, 'E':0, 'S':0, 'W':0}
turnClockwise = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}
turnCounterClockwise = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
direction = 'E'
degrees = 0

for command in lines:
    op, param = command[0:1], int(command[1:])
    if op == 'F':
        grid[direction] += param
    if op == 'L':
        degrees -= param
        while degrees <= -90:
            direction = turnCounterClockwise[direction]
            degrees += 90
    if op == 'R':
        degrees += param
        while degrees >= 90:
            direction = turnClockwise[direction]
            degrees -= 90
    if op == 'N' or op == 'E' or op == 'S' or op == 'W':
        grid[op] += param

print(abs(grid['E']-grid['W']) + abs(grid['N']-grid['S']))