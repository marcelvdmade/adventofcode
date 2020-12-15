def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

file = open('input.txt', 'r') 
lines = file.read()
file.close()

groups = lines.split('\n\n')
count = 0

for group in groups:
    answers = group.split('\n')
    
    if len(answers) == 1:
        count += len(answers[0])
    else:
        yesAnswers = answers[0]
        for answer in answers[1:]:
            yesAnswers = intersection(yesAnswers, answer)
        count += len(yesAnswers)

print(count)