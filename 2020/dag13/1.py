file = open('input.txt', 'r')
lines = file.readlines()
file.close()

arrival = int(lines[0])
buslines = [int(c) for c in lines[1].split(',') if c != 'x']
mods = []

for bus in buslines:
    busCounter = bus
    while busCounter < arrival:
        busCounter += bus
    waitTime = busCounter - arrival
    mods.append((bus, waitTime))

minValue = min(mods, key = lambda t: t[1])
busline = minValue[0]
waitTime = minValue[1]

print(busline * waitTime)