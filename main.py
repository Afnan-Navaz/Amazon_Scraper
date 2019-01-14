from ASINmkr import pageScan
from selenium import webdriver

driver=webdriver.Firefox()
driver.get('https://www.amazon.in/s/ref=sr_pg_1?rh=n%3A976389031%2Ck%3Abook&keywords=book&ie=UTF8&qid=1547433698')
for i in range(76):
	x=driver.current_url
	pageScan(x)
	c=driver.find_element_by_xpath('//span[@id="pagnNextString"]')
	c.click()

driver.close()