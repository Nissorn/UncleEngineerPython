#temp.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv
from datetime import datetime

def writetocsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    with open(f'data-temperature-{date}.csv','a',newline='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)

alldata = {}

def checktemp(city):
    url = 'https://www.yahoo.com/news/weather/thailand/bangkok/bangkok-1225' + str(int(400) + int(city))

    webopen = urlopen(url) #เปิดเว็นโดยไม่ใช้browser
    html_page = webopen.read() #อ่านข้อมูลในเว็บ
    webopen.close() #ปิดเว็บ

    data = BeautifulSoup(html_page,'html.parser') #beautifulsoupแปลงcodeให้

    try:
        temp = data.find('span',{'class':'Va(t) D(n) celsius celsius_D(b)'})
        title = data.find('h1',{'class':'Fz(3rem)--miw1250 Fz(2.65rem)--miw1024 Fz(1.62rem) Fw(n) Lh(1) Trsdu(.3s) Wob(ba)'})

        city = title.text.strip()
        temp = temp.text + str('°C')
        #print(city, temp)
        alldata[city] = str(temp)
        print(i)
    except:
        pass


for i in range(100):
    checktemp(i)
    

#print(alldata)

for k,v in alldata.items():
    data = [k,v]
    writetocsv(data)

print('saved')
