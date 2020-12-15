file = open('input.txt', 'r') 
lines = file.read()
file.close()

groups = lines.split('\n\n')
count = 0
for group in groups:
    answers = group.split('\n')
    combinedList = []
    for answer in answers:
        answerSet = set(answer)
        combinedSet = set(combinedList)
        distinct = list(answerSet - combinedSet)
        combinedList = combinedList + distinct
    count += len(combinedList)

print(count)