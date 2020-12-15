file = open('input.txt', 'r')
lines = file.readlines()
file.close()

def departuresAreSequential(timestamp):
    for i, bus in enumerate(buslines):
        if bus == 0:
            continue
        if (timestamp+i) % bus != 0:
            return False
    return True

buslines = [int(c) for c in lines[1].replace('x', '0').split(',')]
timestamp = 100000000000000

while timestamp < 200000000000000:
    if departuresAreSequential(timestamp):
        break
    timestamp+=1
print(timestamp)