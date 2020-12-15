file = open('input.txt', 'r') 
joltList = [int(line) for line in file.readlines()]
file.close()

jolt1 = 0
jolt3 = 0

joltList.sort() #There are only distinct values in the list
joltage = 0

for jline in joltList:
    result = jline - joltage
    if result == 1:
        jolt1+=1
    if result == 3:
        jolt3+=1
    joltage = jline
jolt3+=1
print(jolt1, jolt3, jolt1 * jolt3)