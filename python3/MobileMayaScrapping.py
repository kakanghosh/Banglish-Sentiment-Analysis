from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time
from pyvirtualdisplay import Display
import io
from selenium.common.exceptions import TimeoutException

url = "https://www.mobilemaya.com"

def getHtml(url):
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, 'html.parser')
    return soup


def getAttributeValue(tagList, attribue):
    hrefList = []
    for anchor in tagList:
        value = anchor.get(attribue)
        hrefList.append("https:"+value)
    return hrefList

def showList(colList):
    for n in colList:
        print(n)
    print()

def writeListInFile(fileName, mode, writeList):
    # print(type(writeList))
    txtFile = io.open(fileName, mode, encoding="utf-8")
    for line in writeList:
        if (type(line) is  list):
            for li in line:
                txtFile.write(''.join(li)+"\n")
            txtFile.write("\n")
        else:
            txtFile.write(''.join(line)+"\n")

    txtFile.write("\n")
    txtFile.close()



def getBrandsAllPaginationUrl(mobileBrandUrl):
    html = getHtml(mobileBrandUrl)
    #print(html.title.string)
    paginationsHTML = html.select("div#pagination > div.pages > a")
    paginationsURLs = getAttributeValue(paginationsHTML, 'href')
    paginationsURLs.insert(0,mobileBrandUrl)
    return paginationsURLs



# html = getHtml(url)
# allMobileBrand = html.select("a.pure-menu-link")
# writeListInFile("allbrand.txt","w",allMobileBrand)
#
# allMobileBrandEntryHref = getAttributeValue(allMobileBrand, 'href')
# writeListInFile("allbrandEntryURL.txt","w",allMobileBrandEntryHref)
#
# allMobileBrandAllHref = []
#
# for href in allMobileBrandEntryHref:
#     allMobileBrandAllHref.append(getBrandsAllPaginationUrl(href))
#
# writeListInFile("allbrandAllURL.txt","w",allMobileBrandAllHref)
#
# for allHref in allMobileBrandAllHref:
#     for href in allHref:
#         mobileLinks = getAttributeValue(getHtml(href).select("div#name > a"), 'href')
#         for mobileLink in mobileLinks:
#             path_to_chromedriver = './chromedriver'
#             driver = webdriver.Chrome(executable_path=path_to_chromedriver)
#             driver.implicitly_wait(10)
#             driver.get(mobileLink)
#
#             comments = driver.find_elements_by_id("say")
#             time.sleep(3)  ## to give the browser time for js to generate content (?)
#             commentList = []
#             for comment in comments:
#                 htmlData = comment.get_attribute('innerHTML')
#                 commentList.append(htmlData)
#
#             writeListInFile("reviews.txt", "a", commentList)
#             driver.close()


def recordReviews(mobilePhoneLinks, fileName):
    display = Display(visible=0, size=(800, 600))
    display.start()
    counter = 0
    for href in mobilePhoneLinks:
        mobileLinks = getAttributeValue(getHtml(href).select("div#name > a"), 'href')
        for mobileLink in mobileLinks:
            try:
                counter += 1
                print("Started: ", mobileLink, " : ", counter)
                path_to_chromedriver = './chromedriver'
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                options.add_argument('window-size=400x150')
                driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=options)
                driver.implicitly_wait(10)
                driver.get(mobileLink)

                comments = driver.find_elements_by_id("say")
                time.sleep(5)  ## to give the browser time for js to generate content (?)
                commentList = []
                for comment in comments:
                    htmlData = comment.get_attribute('innerHTML')
                    commentList.append(htmlData)

                writeListInFile(fileName, "a", commentList)

                driver.close()
                print("Ended: ", mobileLink, " : ", counter)
            except TimeoutException as ex:
                driver.close()
                print("Exception has been thrown. " + str(ex))
    display.stop()
    print("Done with ALL ",fileName," Phones")




# phoneLinks = [
#     # {
#     #     "links": ["https://www.mobilemaya.com/brand/htc/2"],
#     #     "fileName": "HTCMobileReviews.txt"
#     # },
#     {
#         "links": ["https://www.mobilemaya.com/brand/lava","https://www.mobilemaya.com/brand/lava/2"],
#         "fileName": "LavaMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/helio"],
#         "fileName": "HelioMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/alcatel","https://www.mobilemaya.com/brand/alcatel/2"],
#         "fileName": "AlcatelMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/we"],
#         "fileName": "WEMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/lenovo"],
#         "fileName": "LenevoMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/gionee"],
#         "fileName": "GioneelMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/mango"],
#         "fileName": "MangoMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/asus"],
#         "fileName": "AsusMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/okapia","https://www.mobilemaya.com/brand/okapia/2"],
#         "fileName": "OkapiaMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/mycell","https://www.mobilemaya.com/brand/mycell/2"],
#         "fileName": "MyCellMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/blackberry"],
#         "fileName": "BlackBerryMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/motorola"],
#         "fileName": "MotorolaMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/intex"],
#         "fileName": "IntexMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/meizu"],
#         "fileName": "MeizuMobileReviews.txt"
#     },{
#         "links":["https://www.mobilemaya.com/brand/stylus"],
#         "fileName": "StylusMobileReviews.txt"
#     }
#
# ]
#
# for obj in phoneLinks:
#     recordReviews(mobilePhoneLinks=obj["links"], fileName=obj["fileName"])

