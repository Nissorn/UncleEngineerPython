#temp.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

def checktemp(city):
    url = 'https://www.tmd.go.th/weather/province/' + str(city)

    webopen = urlopen(url) #เปิดเว็นโดยไม่ใช้browser
    html_page = webopen.read() #อ่านข้อมูลในเว็บ
    webopen.close() #ปิดเว็บ

    data = BeautifulSoup(html_page,'html.parser') #beautifulsoupแปลงcodeให้

    temp = data.find_all('label',{'id':'lblDryBlubTemperature'})
    title = data.find('h1',{'class':'text-dark1'})

    city = title.text.strip()
    #temp = temp.text
    temp = 32 #สมมุตติไว้เพราะว่าwebกรมอุตุอัพใหม่ตอนนี้ดึงข้อมูลไม่ได้
    print(city, temp)

checktemp(trad)