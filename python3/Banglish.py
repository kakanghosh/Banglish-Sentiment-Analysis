from pyavrophonetic import avro
import io
import re
import enchant

def showLines(lines):
    for line in lines:
        print(line)

def removeLinks(line):
    text = re.sub(r'http\S+', '', line)
    return text

def removeSpecialChar(line):
    text = re.sub(r'[?|$|.|!|*]', r'', line)
    return text

def getUniqueReviews(lines):
    uniqueLines = []
    foundNewLine = False
    for line in lines:
        if len(line.strip()) == 0 and foundNewLine is False:
            uniqueLines.append("")
            foundNewLine = True
        elif line not in uniqueLines:
            line = removeLinks(line)
            line = removeSpecialChar(line)
            uniqueLines.append(line)
            foundNewLine = False
    return uniqueLines

def banglishToBangla(lines):
    banglas = []
    for line in lines:
        banglas.append(avro.parse(line))
    return banglas

def isEnglish(word):
    d = enchant.Dict("en_US")
    return d.check(word)

def getReviews(lines):
    lines = getUniqueReviews(lines)
    review = ""
    reviewList = []
    for line in lines:
        if len(line.strip()) == 0:
            reviewList.append(review)
            review = ""
        else:
            review += line + "\n"
    return reviewList

path = "./refineReviews/AlcatelMobileReviews.txt"
reviews = [line.rstrip('\n') for line in open(path)]

print(getReviews(reviews)[0])