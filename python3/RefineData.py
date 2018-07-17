import os
import io
from bs4 import BeautifulSoup

def showList(colList):
    for n in colList:
        print(n)
    print()

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
    writeListInFile(fileName=refinePath+li, mode="a", writeList=lines)