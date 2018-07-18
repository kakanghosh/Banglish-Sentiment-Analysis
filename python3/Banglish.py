from pyavrophonetic import avro
import re
import enchant
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

result = []

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

def sentimentAnalysis(lines):
    print(lines)
    textBlobTrans = TextBlob(avro.parse(lines))
    lines = str(textBlobTrans.translate(to='en'))
    #lines = str("Good")
    # #print(lines)
    analyze = TextBlob(lines)
    #print('By TextBlob Sentiment analysis')
    #print(analyze.sentiment)
    #
    # print('By vaderSentiment analyzer')
    # analyzer = SentimentIntensityAnalyzer()
    # vs = analyzer.polarity_scores(lines)
    # result.append(vs)

def splitByNewLine(text):

    def spliteLine(line):
        return line.strip().split("\n")

    def spliteBySpace(line):
        return line.strip().split(" ")

    spliters = spliteLine(text)
    # newLine = ""
    # for line in spliters:
    #     for word in spliteBySpace(line):
    #         newLine += word + " "
    #     newLine += "\n"
    # return newLine
    return spliters

refinePath = "./refineReviews/";
reviewsList = os.listdir(refinePath)

reviews = [line.rstrip('\n') for line in open(refinePath+reviewsList[0])]
allReviews = getReviews(reviews)

# for review in allReviews:
#     for rev in splitByNewLine(review):
#         print(rev)
#         sentimentAnalysis(rev)
#         print()

sentimentAnalysis(splitByNewLine(allReviews[0])[0])