file = open('input.txt', 'r')
program = file.read()
file.close

operationsOriginal = [int(x) for x in program.split(',')]
goal = 19690720

for noun in range(0, 100):
    for verb in range(0, 100):
        operations = operationsOriginal[:]
        operations[1] = noun
        operations[2] = verb
        ptr = 0
        while operations[ptr] != goal:
            op = operations[ptr]
            if op == 99:
                break
            if op == 1:
                operations[operations[ptr+3]] = operations[operations[ptr+2]] + operations[operations[ptr+1]]
                ptr +=4
            if op == 2:
                operations[operations[ptr+3]] = operations[operations[ptr+2]] * operations[operations[ptr+1]]
                ptr +=4
        if operations[0] == goal:
            print(100*noun+verb)