from collections import defaultdict, deque

with open('input.txt', 'r') as file:
    starters = [int(c) for c in file.read().split(',')]

spoken = defaultdict(lambda: deque(maxlen=2)) #keep track of two most recent usages
lastSpoken = 0
turn = 1

#parse starting input
for num in starters:
    spoken[num].append(turn)
    turn += 1
    lastSpoken = num

#part1
while turn <= 2020:
    if len(spoken[lastSpoken]) != 2:
        spoken[0].append(turn)
        lastSpoken = 0
    else:
        lastSpoken = max(spoken[lastSpoken]) - min(spoken[lastSpoken])
        spoken[lastSpoken].append(turn)
    turn += 1
print('Part1:', lastSpoken)

#part2
while turn <= 30_000_000:
    if len(spoken[lastSpoken]) != 2:
        spoken[0].append(turn)
        lastSpoken = 0
    else:
        lastSpoken = max(spoken[lastSpoken]) - min(spoken[lastSpoken])
        spoken[lastSpoken].append(turn)
    turn += 1
print('Part2:', lastSpoken)