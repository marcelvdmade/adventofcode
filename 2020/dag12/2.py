file = open('input.txt', 'r')
lines = file.readlines()
file.close()

ship = {'N':0, 'E':0, 'S':0, 'W':0}
waypoint = {'N':1, 'E':10, 'S':0, 'W':0}
turnClockwise = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}
turnCounterClockwise = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
direction = 'E'
degrees = 0

#the current input only has rotates of rot%90=0
def rotateLeft(param):
    rotates = int(param / 90)
    for _ in range(0, rotates):
        tempN = waypoint['N']
        waypoint['N'] = waypoint['E']
        waypoint['E'] = waypoint['S']
        waypoint['S'] = waypoint['W']
        waypoint['W'] = tempN
def rotateRight(param):
    rotates = int(param / 90)
    for _ in range(0, rotates):
        tempN = waypoint['N']
        waypoint['N'] = waypoint['W']
        waypoint['W'] = waypoint['S']
        waypoint['S'] = waypoint['E']
        waypoint['E'] = tempN
#make sure only one of n/s and one of e/w is >0
def updateWaypointer():
    for pair in (['N', 'S'], ['S', 'N'], ['E', 'W'], ['W', 'E']):
        if waypoint[pair[0]] > waypoint[pair[1]] and waypoint[pair[1]] != 0:
            waypoint[pair[0]] -= waypoint[pair[1]]
            waypoint[pair[1]] = 0
def updateShip():
    for pair in (['N', 'S'], ['S', 'N'], ['E', 'W'], ['W', 'E']):
        if ship[pair[0]] > ship[pair[1]] and ship[pair[1]] != 0:
            ship[pair[0]] -= ship[pair[1]]
            ship[pair[1]] = 0

for command in lines:
    op, param = command[0:1], int(command[1:])
    if op == 'F':
        for d in {'N', 'E', 'S', 'W'}:
            ship[d] += param * waypoint[d]
        updateShip()
    if op == 'L':
        rotateLeft(param)
    if op == 'R':
        rotateRight(param)
    if op == 'N' or op == 'E' or op == 'S' or op == 'W':
        waypoint[op] += param
        updateWaypointer()
    # print(op, param)
    # print(direction, degrees)
    # print(ship)
    # print(waypoint)

print(abs(ship['E']-ship['W']) + abs(ship['N']-ship['S']))