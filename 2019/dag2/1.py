file = open('input.txt', 'r')
program = file.read()
file.close

operations = [int(x) for x in program.split(',')]

operations[1] = 12
operations[2] = 2

index = 0
while operations[index] != 99:
    op = operations[index]
    if op == 99:
        break
    if op == 1:
        operations[operations[index+3]] = operations[operations[index+2]] + operations[operations[index+1]]
        index +=4
    if op == 2:
        operations[operations[index+3]] = operations[operations[index+2]] * operations[operations[index+1]]
        index +=4
print(operations[0])