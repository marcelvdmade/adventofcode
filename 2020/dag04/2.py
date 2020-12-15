import re

def special_match(strg, search=re.compile(r'[^a-f0-9]').search):
    return not bool(search(strg))

def validByr(dateString):
    date = int(dateString)
    return date >= 1920 and date <= 2002
def validIyr(dateString):
    date = int(dateString)
    return date >= 2010 and date <= 2020
def validEyr(dateString):
    date = int(dateString)
    return date >= 2020 and date <= 2030
def validHgt(heightString):
    contents = re.findall(r"[^\W\d_]+|\d+", heightString)
    if len(contents) != 2:
        return False
    if contents[1] == "in":
        return int(contents[0]) >= 59 and int(contents[0]) <= 76
    if contents[1] == "cm":
        return int(contents[0]) >= 150 and int(contents[0]) <= 193
def validHcl(hairColorString):
    #a # followed by exactly six characters 0-9 or a-f
    hashtag = hairColorString[0:1]
    number = hairColorString[1:]
    if len(number) != 6:
        return False
    return hashtag == '#' and special_match(number)
def validEcl(colorString):
    return colorString == "amb" or colorString == "blu" or colorString == "brn" or colorString == "gry" or colorString == "grn" or colorString == "hzl" or colorString == "oth"
def validPid(passportIdString):
    return len(passportIdString) == 9

file = open('input.txt', 'r') 
lines = file.read()
file.close()

printDebug = False
validPassports = 0
validEntries = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

passports = lines.split('\n\n')

for passport in passports:
    passport = passport.replace("\n", " ") #get rid of pesky newlines
    passportEntries = []
    passportTuples = []
    invalidEntry = False
    entries = passport.split(" ") #get all entries in a passport
    for entry in entries:
        key, value = entry.split(':')
        #if key != 'cid':    #skip this for now
        passportEntries.append(key)
        passportTuples.append((key, value))
    intersection = validEntries.intersection(passportEntries)
    if len(intersection) != len(validEntries):
        continue
    for keyValue in passportTuples:
        if keyValue[0] == "byr":
            if not validByr( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid byr")
        if keyValue[0] == "iyr":
            if not validIyr( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid iyr")
        if keyValue[0] == "eyr":
            if not validEyr( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid eyr")
        if keyValue[0] == "hgt":
            if not validHgt( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid hgt")
        if keyValue[0] == "hcl":
            if not validHcl( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid hcl")
        if keyValue[0] == "ecl":
            if not validEcl( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid ecl")
        if keyValue[0] == "pid":
            if not validPid( keyValue[1]):
                invalidEntry = True
                if printDebug:
                    print("invalid pid")
    if not invalidEntry:
        validPassports += 1
    if printDebug and invalidEntry:
        print(passport)

print(validPassports)