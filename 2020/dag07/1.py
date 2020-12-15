from collections import defaultdict, deque

rules = {}
with open('input.txt','r') as file_:
    for line in file_:
        s = line.strip().split(' bags contain ')
        content = defaultdict(int)
        for comp in s[1].split(', '):
            words = comp.split(' ')
            if words[0] != 'no':
                content[words[1] + ' ' + words[2]] = int(words[0])
        rules[s[0]] = content

bags = set(['shiny gold'])
length = 0

while len(bags) > length:
    length = len(bags)
    [bags.add(key) for key in rules if any(color in rules[key].keys() for color in bags)]
    
print(len(bags)-1)