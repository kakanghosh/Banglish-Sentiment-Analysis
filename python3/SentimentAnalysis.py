import os
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

result = []

def showLines(lines):
    for line in lines:
        print(line)

def countLine(lineList):
    counter = 0
    for line in lineList:
        if len(line.strip()) > 0:
            counter += 1
    return counter

def writeLineInFile(fileName, mode, line):
    txtFile = open(fileName, mode, encoding="utf-8")
    txtFile.write(line + "\n")
    txtFile.close()

def sentimentAnalysis(fileName,lines):
    lineList = lines.splitlines()
    counter = 0

    if os.path.isfile(fileName) and os.access(fileName, os.R_OK):
        open(fileName, "w").close()
    textSentiList = []
    vaderSeltiList = []
    for line in lineList:
        if len(line.strip()) > 0:
            analyze = TextBlob(line)
            textSenti = analyze.sentiment

            analyzer = SentimentIntensityAnalyzer()
            vs = analyzer.polarity_scores(line)
            counter += 1

            writeLineInFile(fileName=fileName, mode='a', line=line)
            writeLineInFile(fileName=fileName, mode='a', line=repr(textSenti))
            writeLineInFile(fileName=fileName, mode='a', line=repr(vs))
            writeLineInFile(fileName=fileName, mode='a', line="")

            textSentiList.append(textSenti)
            vaderSeltiList.append(vs)
    result.append({
        fileName : {
            'totalLine' : counter,
            'textblobs' : textSentiList,
            'vaders' : vaderSeltiList
        }
    })


englishReviewsPath = "./englishReviews/"
sentimentPath = "./sentiment/"
fileList = os.listdir(englishReviewsPath)
fileList.sort()


for file in fileList:
    lines = [line.rstrip('\n') for line in open(englishReviewsPath + file)]
    lines = '\n'.join(lines)
    sentimentAnalysis(fileName=sentimentPath+file,lines=lines)

for res in result:
    for key in res.keys():
        resObj = res[key]
        totalLines = resObj['totalLine']
        textblobs = resObj['textblobs']
        vaders = resObj['vaders']
        textBlobCal = {'polarity' : 0,'subjectivity' : 0}
        vaderCal = {'neg': 0, 'pos': 0, 'neu' : 0, 'compound' : 0}
        for textObj in textblobs:
            textBlobCal['polarity'] += textObj.polarity
            textBlobCal['subjectivity'] += textObj.subjectivity

        for vaderObj in vaders:
            vaderCal['neg'] += vaderObj['neg']
            vaderCal['pos'] += vaderObj['pos']
            vaderCal['neu'] += vaderObj['neu']
            vaderCal['compound'] += vaderObj['compound']

        print('\n\nResult of', key)

        print('\nTextBlob')
        print('Avarage Polarity: ',textBlobCal['polarity'] / totalLines)
        print('Avarage Subjectivity: ',textBlobCal['subjectivity'] / totalLines)
        print('\n\nVaderSentiment')
        print('Avarage Positive: ', vaderCal['pos'] / totalLines)
        print('Avarage negative: ', vaderCal['neg'] / totalLines)
        print('Avarage Neutral: ', vaderCal['neu'] / totalLines)
        print('Avarage Compound: ', vaderCal['compound'] / totalLines)

