from bs4 import BeautifulSoup
import requests

link=input("ASIN: ")
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
url=requests.get('https://www.amazon.in/dp/'+link+'?tag=YOURASSOCIATEID', headers=headers).text
soup=BeautifulSoup(url, 'lxml')
if soup.find('h1', id='title').span['id'] == "productTitle":
	xid='productTitle'
else:
	xid='ebooksProductTitle'
print("*"*40)
print("TITLE = "+soup.find('span', id=xid).text)
print("AUTHOR = "+soup.find('a', class_='contributorNameID').text)
print("NO OF REVIEWS = "+soup.find('span', id='acrCustomerReviewText').text)
print("RATING = "+soup.find('span', id='acrPopover')['title'])
price=soup.find('div', id='twister').find_all('div', class_='top-level')
for i in price:
	print(i.find('span', class_='a-color-base').text+" = "+i.find('span', class_='a-color-price').text)
prodet=soup.find('div', id='detail_bullets_id').ul.find_all('li')
for pro in prodet:
	prod=str(pro.text).split(" ")
	if len(prod)==2:
		print(prod[0]+" = "+prod[1])

