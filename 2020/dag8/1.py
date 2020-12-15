file = open('input.txt', 'r') 
lines = file.readlines()
file.close()

acc = 0
linesExecuted = []
lineNumber = 0

while True:
    if lineNumber in linesExecuted:
        break
    line = lines[lineNumber]
    op = line[0:3]
    sign = line[4:5]
    num = int(line[5:])
    linesExecuted.append(lineNumber)
    if op == "nop":
        lineNumber+=1
    if op == "jmp":
        if sign == "+":
            lineNumber+=num
        else:
            lineNumber-=num
    if op == "acc":
        lineNumber+=1
        if sign == "+":
            acc+=num
        else:
            acc-=num

print(acc)