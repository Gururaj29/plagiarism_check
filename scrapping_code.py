from selenium import webdriver
import os
import time
import sys

driver = webdriver.Chrome('/Users/gkulkarni/Applications/chromedriver/2.45/chromedriver')
lang_code = {"cpp": 44, "c": 11, "py": 116}

contest_name = sys.argv[1]
question_name = sys.argv[2]
language = sys.argv[3]
lcode= lang_code[language]
pages = sys.argv[4] if len(sys.argv)>4 else 1

driver.get('https://www.codechef.com/%s/status/%s?sort_by=All&sorting_order=asc&language=%s&status=15&handle=&Submit=GO' %(contest_name, question_name, lcode))

path = "dataset/scrapped_codes/" + contest_name + '-' + question_name
os.system("mkdir -p " + path)

path += '/' + language
os.system("mkdir -p " + path)


table_rows_len = len(driver.find_elements_by_xpath("//div[@id='primary-content']/div/div[3]/table/tbody/tr"))

print(table_rows_len)
for row in range(1,table_rows_len+1):
	#driver.get('https://www.codechef.com/%s/status/%s?sort_by=All&sorting_order=asc&language=%s&status=15&handle=&Submit=GO' %(contest_name, question_name, "44"))
	coder_name = driver.find_element_by_xpath("//div[@id='primary-content']/div/div[3]/table/tbody/tr[%s]/td[3]" %(row)).text[2:]
	driver.find_element_by_xpath("//div[@id='primary-content']/div/div[3]/table/tbody/tr[%s]/td[8]/ul/li/a" %(row)).click()
	time.sleep(1)
	driver.switch_to.window(driver.window_handles[1])

	File = path + '/' + coder_name + '.' + language
	with open(File, 'w') as file:
		file.write(driver.find_element_by_xpath("//section[@id='solution_app']/div/section[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]").text)
	driver.close()
	time.sleep(1)
	#driver.close()
	driver.switch_to.window(driver.window_handles[0])
	driver.execute_script("window.scrollBy(0,100);")

