from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import json
base_url = 'http://maoyan.com/board/4?offset='

headers = {
	'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
def getHTML(base_url,offset):
	url = base_url + str(offset)
	try:
		response = requests.get(url,headers = headers)
	except requests.HTTPError as e:
		return None
	else:
		return response.text

def parseHTML(html):
	soup = BeautifulSoup(html,'lxml')
	dd = soup.find_all('dd')
	for item in dd:
		yield {
			'index':item.select('.board-index')[0].get_text(),
			'name':item.select('.name')[0].get_text(),
			'star':item.select('.star')[0].get_text().strip(),
			'releasetime':item.select('.releasetime')[0].get_text()[5:],
			'score':item.select('.score')[0].get_text()
		}

def write_to_file(content):
	with open('maoyan_result.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii=False) + '\n')
		f.close()

def main(offset):
	for item in parseHTML(getHTML(base_url,offset)):
		print(item)
		write_to_file(item)
if __name__ == "__main__":
	for i in range(0,100,10):
		for item in parseHTML(getHTML(base_url,i)):
			print(item)
			write_to_file(item)
	# pool = Pool()
	# pool.map(main,[i for i in range(0,100,10)])