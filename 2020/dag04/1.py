import re

file = open('input.txt', 'r') 
lines = file.read()
file.close()

validPassports = 0
validEntries = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

passports = lines.split('\n\n')

for passport in passports:
    passport = passport.replace("\n", " ") #get rid of pesky newlines
    passportEntries = []
    entries = passport.split(" ") #get all entries in a passport
    for entry in entries:
        key, value = entry.split(':')
        passportEntries.append(key)
    intersection = validEntries.intersection(passportEntries)
    if len(intersection) == len(validEntries):
        validPassports += 1

print(validPassports)