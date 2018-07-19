from pyavrophonetic import avro
import re
import enchant
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
from googletrans import Translator
import io

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


def writeListInFile(fileName, mode, writeList):
    # print(type(writeList))
    if os.path.isfile(fileName) and os.access(fileName, os.R_OK):
        open(fileName, "w").close()

    txtFile = open(fileName, mode, encoding="utf-8")
    for line in writeList:
        txtFile.write(line+"\n")
    txtFile.close()

def banglaToEnglish(banglText):
    translator = Translator()
    lines = translator.translate(avro.parse(banglText))
    print(lines)
    return lines.text

refinePath = "./refineReviews/"
phoneticsReviewsPath = "./englishReviews/"
fileList = os.listdir(refinePath)
fileList.sort()

# for file in fileList:
#     lines = [line.rstrip('\n') for line in open(refinePath + file)]
#     lines = '\n'.join(lines)
#     banglaToEnglish(str(lines))
#     break

    #writeListInFile(fileName=phoneticsReviewsPath+file, mode="a", writeList=banglishToBangla(lines))
