import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.boc.cn/sourcedb/whpj/')
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text,'lxml')
target = soup.select('.publish table')[1].select('tr')[12].select('td')[4].text
print(target)

# body > div.wrapper > div.BOC_main > div.publish > div:nth-child(3) > table > tbody > tr:nth-child(13) > td:nth-child(4)