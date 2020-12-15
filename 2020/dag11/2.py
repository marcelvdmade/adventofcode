def countJoltages(joltages):
    compatible = {}
    for i, joltage in enumerate(joltages[:-1]):
        print(i, joltage)
        compatible[joltage] = [j for j in joltages[i+1:i+4] if j - joltage <= 3]

    arrangements = {joltages[-1]: 1}
    for joltage in reversed(joltages[:-1]):
        arrangements[joltage] = sum(arrangements[j] for j in compatible[joltage])

    return arrangements[outletJoltage]

file = open('input.txt', 'r') 
joltList = [int(line) for line in file.readlines()]
file.close()

outletJoltage = 0

adapters = sorted(joltList)
joltages = [outletJoltage] + adapters + [adapters[-1] + 3]

print(countJoltages(joltages))