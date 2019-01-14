from selenium import webdriver
driver=webdriver.Firefox()

driver.get('https://www.amazon.in/s/ref=sr_pg_2?rh=n%3A976389031%2Ck%3Abook&page=2&d=1&keywords=book&ie=UTF8&qid=1547399543')
for i in range(76):
	c=driver.find_element_by_xpath('//span[@id="pagnNextString"]')
	c.click()


driver.close()
