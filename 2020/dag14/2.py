import re
from collections import defaultdict

with open('input.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    res = defaultdict(list)
    for line in data.split('\n'):
        if line[:4] == 'mask':
            mask = line[-36:]
        if line[:3] =='mem':
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            res[mask].append((int(match.group(1)), int(match.group(2))))
    return res

def bitmask(mask, num):
    num = bin(num)[2:].zfill(36)
    res = []
    count = mask.count('X')
    new = ''.join('{}' if v=='X' else '1' if v=='1' else num[i] for i, v in enumerate(mask))
    for n in range(2**count):
        n = bin(n)[2:].zfill(count)
        res.append(new.format(*n))
    return [int(x, 2) for x in res]

data = parse_input(data)
result = {}

for mask, ints in data.items():
    for k, v in ints:
        for address in bitmask(mask, k):
            result[address] = v

print(sum(result.values()))