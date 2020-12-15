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

bags = defaultdict(int)
queue = deque([('shiny gold',1)])

while len(queue) > 0:
    color, amount = queue.pop()
    for key in rules[color]:
        queue.append((key, rules[color][key] * amount))
        bags[key] += rules[color][key] * amount

print(sum(bags.values()))