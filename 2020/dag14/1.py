import re
from collections import defaultdict

with open('input.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    result = defaultdict(list)
    for line in data.split('\n'):
        if line[:4] == 'mask':
            mask = line[-36:]
        if line[:3] =='mem':
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            result[mask].append((int(match.group(1)), int(match.group(2))))
    return result

def bitmask(mask, number):
    number = bin(number)[2:].zfill(36)
    res = [number[i] if v=='X' else v for i, v in enumerate(mask)]
    return int(''.join(res), 2)

data = parse_input(data)
res = {}

for mask, ints in data.items():
    for k, v in ints:
        res[k] = bitmask(mask, v)

print(sum(res.values()))