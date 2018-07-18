from pyavrophonetic import avro
import re
import enchant
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
from googletrans import Translator

textBlobresult = []
vaderSentimentResult = []

def showLines(lines):
    for line in lines:
        print(line)


def banglishToBangla(lines):
    banglas = []
    for line in lines:
        banglas.append(avro.parse(line))
    return banglas

def isEnglish(word):
    d = enchant.Dict("en_US")
    return d.check(word)



def sentimentAnalysis(linesCollection):
    if len(linesCollection.strip()) is not 0:
        translator = Translator()
        lines = translator.translate(avro.parse(linesCollection))
        #print(lines.text)
        analyze = TextBlob(str(lines.text))
        textBlobresult.append(analyze.sentiment)
        #
        # analyzer = SentimentIntensityAnalyzer()
        # vs = analyzer.polarity_scores(lines)
        # vaderSentimentResult.append(vs)

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

refinePath = "./refineReviews/"
phoneticsReviewsPath = "./phoneticsReviews/"
reviewsList = os.listdir(refinePath)

reviews = [line.rstrip('\n') for line in open(refinePath+reviewsList[0])]
showLines(reviews)
# allReviews = getReviews(reviews)
#
#
# for review in allReviews:
#     for rev in splitByNewLine(review):
#         print(rev)
#         sentimentAnalysis(rev)
#         print()
#
#
#
# showLines(textBlobresult)
# print()
# showLines(vaderSentimentResult)