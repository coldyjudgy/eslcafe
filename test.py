# EMAIL DECODING TEST

import requests
url = 'https://www.eslcafe.com/postajob-detail/direct-hire-full-time-english-teacher-9001800-8?koreasearch=&koreapageno=3&koreapagesize=60&chinasearch=&chinapageno=&chinapagesize=&internationalsearch=&internationalpageno=&internationalpagesize='
res = requests.get(url)

def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

from bs4 import BeautifulSoup as bs

def second():
    soup = bs(res.text, 'html.parser')
    tags = soup.select('.author-desc')
    email = soup.select_one("[class='__cf_email__']").get("data-cfemail")
    name = soup.select_one("[class='__cf_email__']").get("data-cfemail")

    #print(tags)
    for tag in tags:
        # print(tag.text)
        return(cfDecodeEmail(email))

second()

