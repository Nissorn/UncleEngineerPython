#writecsv.py

import csv
from datetime import datetime

def writetocsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    with open(f'data-temperature-{date}.csv','a',newline='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)

'''
a = append ไฟล์จะส่งออกและเพิ่มค่าไปเก็บในไฟล์นี้เรื่อยๆ
w = เขียนdataทั้งก้อน เหมาะกันการเพิ่มค่าเรื่อยๆ
newline='' เพื่อมีพื้นที่ว่าง
'''

writetocsv(['adsf',31])