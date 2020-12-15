with open("input.txt") as f:
    lines = f.readlines()

buslines = list(map(lambda x: x if x=='x' else int(x), lines[1].strip().split(',')))
idmap = {key:val for val, key in filter(lambda x: x[1]!='x', enumerate(buslines))}
busIdList = [id for id in idmap]
print(idmap)

start = 0
step = busIdList[0]

for id in busIdList[1:]:
    delta = idmap[id]
    for i in range(start, step*id, step):
        if not (i+delta)%id:
            step = step*id
            start = i    
print(start)