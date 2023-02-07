import os
import re
import random
import time
import datetime
import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
url = 'http://www.stockq.org/market/commodity.php'
webpage = requests.get( url, headers = HEADERS, cookies={'over18':'1'})
 # 建立連線 : http://www.stockq.org/market/commodity.php
 # print(webpage) # 檢查是否連結上該網站(ex : 404 = not found, 200 =正常 )

soup = BeautifulSoup(webpage.text,'html.parser')
while True:        
    bs4_name_roe2 = soup.find_all('tr', class_='row2')
    # print(str(bs4_name[2]))  # 抓網頁的html碼
    if re.findall('nowrap="">(.*?)<', str(bs4_name_roe2[2])):
        price_cu = re.findall('nowrap="">(.*?)<', str(bs4_name_roe2[2]))[1]
        print(price_cu)
        reptile_time_cu = re.findall('nowrap="">(.*?)<', str(bs4_name_roe2[2]))[4]
        print(reptile_time_cu)
    else :print('can\'t find Cu')
     # 字串處理找到要的東西
     
    soup = BeautifulSoup(webpage.text,'html.parser')        
    bs4_name_row1 = soup.find_all('tr', class_='row1')
    # print(str(bs4_name_ni))  # 反簡易防爬蟲 抓網頁的html碼  
    if re.findall('nowrap="">(.*?)<', str(bs4_name_row1[3])):
        price_ni = re.findall('nowrap="">(.*?)<', str(bs4_name_row1[3]))[1]
        print(price_ni)
        reptile_time_ni = re.findall('nowrap="">(.*?)<', str(bs4_name_row1[3]))[4]
        print(reptile_time_ni)
    else :print('can\'t find Ni')
      # 字串處理找到要的東西
    date = datetime.date.today()
    # print(date)
    fn = 'StockQ'+ str(date) +'.csv'
            
    if os.path.exists(fn):
        pass
    else:
        title = '''時間, 銅的價格, 鎳的價格,\n''' 
        with open(fn,'w') as file_Obj:
            work = file_Obj.write(title)
    
    content = str(reptile_time_cu) +', '+ str(price_cu) +', '+ str(price_ni)+'\n'
    with open(fn,'a') as file_Obj:
        work = file_Obj.write(content)
    time.sleep(1800)
