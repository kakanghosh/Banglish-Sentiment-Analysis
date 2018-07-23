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
    text = re.sub(r'[?|$|.|!|*|=|_]', r'', line)
    return text

def getUniqueReviews(lines):
    resultList = []
    counter = 0
    newLine = False
    for line in lines:
        if len(line.strip()) == 0 and newLine is True:
            resultList.append('\n')
            counter += 1
            newLine = False
            pass
        elif line.strip() not in resultList:
            line = line.strip()
            line = removeLinks(line)
            line = removeSpecialChar(line)
            line = removeTags(line)
            resultList.append(line.strip())
            newLine = True
    return resultList

# def getReviews(lines):
#     lines = getUniqueReviews(lines)
#     review = ""
#     reviewList = []
#     for line in lines:
#         if len(line.strip()) == 0:
#             reviewList.append(review)
#             review = ""
#         else:
#             review += line + "\n"
#     return reviewList

def removeTags(lines):
    return BeautifulSoup(lines, "lxml").text

def writeListInFile(fileName, mode, writeList):
    # print(type(writeList))
    open(fileName, "w").close()
    txtFile = io.open(fileName, mode, encoding="utf-8")
    for line in writeList:
        txtFile.write(removeTags(line)+"\n")
    txtFile.close()

folderPath = "./reviews/";
refinePath = "./refineReviews/";

reviewsList = os.listdir(folderPath)
reviewsList.sort()


for li in reviewsList:
    lines = open(folderPath+li).readlines()
    lines = getUniqueReviews(lines)
    writeListInFile(fileName=refinePath+li, mode="a", writeList=lines)