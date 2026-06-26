import requests
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



class Main():
    def __init__(self):
        self.base = 'https://xkcd.com/'
        self.req=0
        self.comicNumber = self.findComicNumber()
        self.findImage()
        self.showImage()
    def findComicNumber(self):
        f = open('Data.txt').read()
        dat = f.split('\n')
        dat = int(dat[0])
        hasFound= False
        while(not hasFound):
            #print(requests.get(self.base + str(dat) +'/') )
            if(requests.get(self.base + str(dat) +'/').status_code == 404):
                #print("Found most recent comic!")
                dat-=1
                hasFound=True
            else:
                dat+=1
        f = open('Data.txt','w')
        f.write(str(dat))
        self.req=requests.get(self.base + str(dat) +'/') 
    def findImage(self):
        soup = BeautifulSoup(self.req.text,'html.parser')
        #print(soup.prettify())
        arr = None
        for link in soup.find_all('a'):
            #print(link.get('href'))
            arr=(link.get('href'))
            if("imgs" in arr):
                print(arr)
                break
        imgreq = requests.get(arr)
        with open('comic.png','wb') as f:
            f.write(imgreq.content)
    def showImage(self):
        img = mpimg.imread('comic.png')
        imgplot = plt.imshow(img)
        plt.show()
        


Main()