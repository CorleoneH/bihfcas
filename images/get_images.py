import requests
from bs4 import BeautifulSoup
import bs4
import os

def getHTMLText(url, encoding='utf-8'):
    try:    
        r = requests.get(url)
        r.encoding = encoding
        r.raise_for_status()
        return r.text
    except:
        return ""

def getLink(html, url, linkInfos):
    soup = BeautifulSoup(html, 'lxml')
    #Find all the Tags named img
    infos = soup.find_all('img')
    for info in infos:
        #avoid NoneType Tag
        if isinstance(info, bs4.element.Tag):
            linkInfos.append(url + info['src'])
    print("Find " + str(len(linkInfos)) + " image links!\n")

def saveToFile(root, linkInfos):
    for linkInfo in linkInfos:
        num = linkInfos.index(linkInfo) + 1
        path = root + linkInfo.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(linkInfo)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(str(num) + '. File save successfully!')
            else:
                print(str(num) + ". File already exists!")
        except:
            print("Get something wrong!")

def main():
    url = "http://www.bihfcas.net/"
    root = "F:/Images/bihfcas/"

    html = getHTMLText(url)
    linkList = []
    getLink(html, url, linkList)
    saveToFile(root, linkList)

    print("\nSuccess!")

main()
