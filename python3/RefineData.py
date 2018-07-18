import os
import io
from bs4 import BeautifulSoup
import re

def showList(colList):
    for n in colList:
        print(n)
    print()

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

def removeTags(lines):
    return BeautifulSoup(lines, "lxml").text

def writeListInFile(fileName, mode, writeList):
    # print(type(writeList))
    txtFile = io.open(fileName, mode, encoding="utf-8")
    for line in writeList:
        txtFile.write(removeTags(line)+"\n")
    txtFile.close()

folderPath = "./reviews/";
refinePath = "./refineReviews/";

reviewsList = os.listdir(folderPath)

for li in reviewsList:
    lines = [line.rstrip('\n') for line in open(folderPath+li)]
    lines = getReviews(lines)
    writeListInFile(fileName=refinePath+li, mode="a", writeList=lines)