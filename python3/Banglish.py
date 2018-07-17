from pyavrophonetic import avro
import io
import re
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
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

def getUniqueLines(lines):
    uniqueLines = []
    foundNewLine = False
    for line in lines:
        if line is "" and foundNewLine is False:
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

path = "./refineReviews/AlcatelMobileReviews.txt"
reviews = [line.rstrip('\n') for line in open(path)]

uniqueLines = getUniqueLines(reviews)

print(isEnglish(uniqueLines[0]))
c = TextBlob(uniqueLines[0])
print(c)
print(c.translate(to="BN"))