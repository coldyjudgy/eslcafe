import time
import requests

# EDIT HERE
country = 'international'
pageNo = '3'

url = 'https://www.eslcafe.com/jobs/{}?{}pageno={}'.format(country, country, pageNo) 
# print(url)
# https://www.eslcafe.com/jobs/korea?koreapageno=1

# dynamic scrapping
from selenium import webdriver as wd
driver = wd.Chrome(executable_path = './chromedriver')
driver.implicitly_wait(2)
driver.get(url)
time.sleep(1)
driver.execute_script("loadJobBoardList()") # get data
time.sleep(1)
html = driver.page_source

from bs4 import BeautifulSoup as bs
soup = bs(html, 'html.parser')
# print(soup)

# COMPANY NAME
names = soup.find_all("p",class_="ng-binding")
for nm in names:
    print(nm.text)

# REF
def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

#refs = soup.find('div', class_='job-title').find_all("a", class_="ng-binding")
refs = soup.find_all("a", class_="ng-binding")
for ref in refs:
    #print(ref['href'])
    try:
        url = 'https://www.eslcafe.com' + ref['href']
        # print(url)
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        tags = soup.select('.job-detail-wrap')
        #tags = soup.select('.body')
        email = soup.select_one("[class='__cf_email__']").get("data-cfemail")

        #print(tags)
        for tag in tags:
            res = cfDecodeEmail(email)
            print(res)
            # print(tag.text)

    except Exception as e:
        print(e)
        continue
