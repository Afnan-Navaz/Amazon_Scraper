from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import random
import re
from torrequest import TorRequest

def pageSpr(link):
	dic={}
	ua = UserAgent()
	headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36 ua.random'}
	tr=TorRequest(1234)
	tr.reset_identity()
	url=requests.get('https://www.amazon.in/dp/'+str(link)+'?tag=YOURASSOCIATEID', headers=headers).text
	soup=BeautifulSoup(url, 'lxml')
	try:
		if soup.find('h1', id='title').span['id'] == "productTitle":
			xid='productTitle'
		else:
			xid='ebooksProductTitle'
	except (AttributeError, TypeError):
		pass
	try:
		dic["TITLE"]=soup.find('span', id=xid).text
	except (AttributeError, TypeError, UnboundLocalError):
		dic["TITLE"]=" "
		pass
	try:
		dic["AUTHOR"]=soup.find('a', class_='contributorNameID').text
	except (AttributeError, TypeError):
		dic["AUTHOR"]=" "
		pass
	try:
		dic["NO OF REVIEWS"]=soup.find('span', id='acrCustomerReviewText').text
	except (AttributeError, TypeError):
		dic["NO OF REVIEWS"]=" "
		pass
	try:
		dic["RATING"]=soup.find('span', id='acrPopover')['title']
	except (AttributeError, TypeError):
		dic["RATING"]=" "
		pass
	try:
		price=soup.find('div', id='twister').find_all('div', class_='top-level')
	except (AttributeError, TypeError):
		pass
	try:
		for i in price:
			try:
				dic[i.find('span', class_='a-color-base').text]=i.find('span', class_='a-color-price').text
			except (AttributeError, TypeError):
				continue
	except (UnboundLocalError):
		pass
	try:
		prodet=soup.find('div', id='detail_bullets_id').ul.find_all('li')
	except (AttributeError, TypeError, ValueError):
		pass
	try:
		for pro in prodet:
			try:
				prod=str(pro.text).split(" ")
				if len(prod)==2:
					dic[prod[0]]=[prod[1]]
			except (AttributeError, TypeError, ValueError):
				continue
	except (UnboundLocalError):
		pass
	return dic
