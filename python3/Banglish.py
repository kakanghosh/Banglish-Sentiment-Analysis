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

def writeLineInFile(fileName, mode, line):
    txtFile = open(fileName, mode, encoding="utf-8")
    txtFile.write(line + "\n")
    txtFile.close()

def banglaToEnglish(banglaText):
    englishList = []
    textLineList = banglaText.splitlines()
    for line in textLineList:
        translator = Translator()
        lines = translator.translate(avro.parse(line))
        englishList.append(lines.text)
    return englishList

def banglaToEnglish(banglaText, fileName, mode):
    englishList = []
    textLineList = banglaText.splitlines()

    if os.path.isfile(fileName) and os.access(fileName, os.R_OK):
        open(fileName, "w").close

    for line in textLineList:
        try:
            translator = Translator()
            lines = translator.translate(avro.parse(line))
            englishList.append(lines.text)
            writeLineInFile(fileName, mode, lines.text)
        except Exception as e:
            print("type error: " + str(e))
    return englishList

refinePath = "./refineReviews/"
englishReviewsPath = "./englishReviews/"
fileList = os.listdir(refinePath)
fileList.sort()

for file in fileList:
    lines = [line.rstrip('\n') for line in open(refinePath + file)]
    lines = '\n'.join(lines)
    englishList = banglaToEnglish(str(lines), fileName=(englishReviewsPath + file), mode='a')
