file = open('input.txt', 'r') 
lines = file.readlines()
file.close()

acc = 0

for i in range(0, len(lines)):
    newLines = lines[:]
    if newLines[i][0:3] == "jmp":
        newLines[i] = newLines[i].replace("jmp", "nop")
    lineNumber = 0
    acc = 0
    linesExecuted = []
    while True:
        if lineNumber in linesExecuted or lineNumber < 0 or lineNumber >= len(lines):
            break
        line = newLines[lineNumber]
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
    if lineNumber == len(lines):
        print(acc)
