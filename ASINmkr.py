from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import requests
import random
import re
from torrequest import TorRequest

def pageScan(link):

	li=[]
	ua = UserAgent()
	headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36 ua.random'}
	tr=TorRequest(1234)
	tr.reset_identity()
	url=tr.get(link).text

	soup=BeautifulSoup(url, 'lxml')
	try:
		links=soup.find('div', id='atfResults').find('ul', id='s-results-list-atf').find_all('li', class_='s-result-item')
		for l in links:
			li.append(l['data-asin'])
	except (AttributeError, TypeError):
		pass
	return li