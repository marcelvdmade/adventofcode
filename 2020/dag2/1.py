file = open('input.txt', 'r') 
lines = file.readlines()
file.close()

correctPasswords = 0

for line in lines:
    firstHalf, password = line.split(': ')
    secondHalf, char = firstHalf.split(' ')
    minAmount, maxAmount = secondHalf.split('-')
    minAmount = int(minAmount)#ez mode
    maxAmount = int(maxAmount)
    firstPos = password[minAmount-1:minAmount] == char
    secondPos = password[maxAmount-1:maxAmount] == char
    if not (firstPos and secondPos) and (firstPos or secondPos):
        correctPasswords +=1

print(correctPasswords)