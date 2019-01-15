from ASINmkr import pageScan
from selenium import webdriver
from data import pageSpr
import csv

cs=open("result.csv", mode="w")
fieldnames=['TITLE','AUTHOR','NO OF REVIEWS','RATING','Kindle Edition','Hardcover','Paperbac','Language:','ISBN-10:','ISBN-13:','ASIN:']
writer=csv.DictWriter(cs, fieldnames=fieldnames, extrasaction='ignore')
writer.writeheader()
driver=webdriver.Firefox()
driver.get('https://www.amazon.in/s/ref=sr_pg_1?rh=n%3A976389031%2Ck%3Abook&keywords=book&ie=UTF8&qid=1547433698')
for i in range(76):
	x=driver.current_url
	y=pageScan(x)
	for l in y:
		writer.writerow(pageSpr(l))
	c=driver.find_element_by_xpath('//span[@id="pagnNextString"]')
	c.click()

driver.close()
cs.close()
