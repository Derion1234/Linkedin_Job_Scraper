from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

#YOUR USER AND PASSWORD

user_linkedin = 'your_linkedin_user'
passw_linkedin = 'your_linkedin_password'

driver = webdriver.Chrome()

#LINKEDIN LOGIN SECTION

driver.get('https://www.linkedin.com/login/es')
time.sleep(2)

#FIND INPUT FOR USER AND PASSWORD AND THE LOGIN BUTTON

input_user = driver.find_element_by_id('username')
input_passw = driver.find_element_by_id('password')
login_button = driver.find_element_by_tag_name('button')


#ENTER USER AND PASSWORD IN THEIR RESPECTIVE INPUTS, THEN IT PRESS "LOGIN" BUTTON

input_user.send_keys(user_linkedin)
input_passw.send_keys(passw_linkedin)

try:

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, 'password'))
		)
finally:

	login_button.click()
	time.sleep(10)

#REDIRECT TO JOB SECTION, WITH KEYWORD "Python", YOU CAN CHANGE THIS TO WHATEVER YOU WANT

driver.get('https://www.linkedin.com/jobs/search/?keywords=Python')
time.sleep(5)


#FIND "LI" TAG FROM EVERY JOB

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
all_jobs = soup.find_all('li', class_="jobs-search-results__list-item occludable-update p0 relative ember-view")


#FUNCTION THAT FILTERS JOB_IMAGE, JOB TITLE, ETC.. FROM "all_jobs" AND CONVERTS THE DATA INTO PYTHON OBJECTS

def li_html_to_obj(job_html):
	job_image = job_html.find("img")['src']
	job_title = job_html.find(class_='disabled ember-view job-card-container__link job-card-list__title')
	company_name = job_html.find(class_='artdeco-entity-lockup__subtitle ember-view')
	job_release = job_html.find("time")['datetime']
	job_url = job_html.find("a")['href'].split('&')

	#RECORT JOB_URL
	i = 0
	len_list = len(job_url)
	while i < (len_list - 1):
		job_url.pop()
		i += 1

	#URL LISTO TO STRING
	job_url = ''.join([str(elem) for elem in job_url])

	#RETURN JOBS IN HTML FORMAT TO PYTHON OBJECTS

	return {"image_url" : job_image, "job title" :  job_title.text.strip(),
	"company name" : company_name.text.strip(), "job url" : 'https://www.linkedin.com'+job_url,
	"job_release" : job_release}


import send_gmail
import dbcontrol

call_sql = dbcontrol.select_sql()



for job_li_html in all_jobs:
	job_obj = li_html_to_obj(job_li_html)

	# IF THE JOB_OBJ IS NOT IN THE DATABASE, IT WILL BE UPLOADED TO THE DATABASE AND WILL SEND YOU AN EMAIL WITH ALL THE JOB INFORMATION.
	if job_obj in call_sql:

		print('THIS JOB IS ALREADY IN DB')

	else:

		dbcontrol.insert_sql(job_obj)
		send_gmail.envia_mail(job_obj)