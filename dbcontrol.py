import mysql.connector
from config import *


#CONNECT TO DATABASE
fulltien_dario = mysql.connector.connect(
	host = db_connection_data['host'],
	user = db_connection_data['user'],
	password = db_connection_data['password'],
	database = db_connection_data['database']
	)
	
mycursor = fulltien_dario.cursor()


#SELECT ALL DATA FROM YOUR DB TABLE AND RETURNS IT AS A PYTHON OBJECT, WITH THE SAME ORDER AS li_html_to_obj() FUNCTION RETURNS JOBS.
def select_sql():

	sql_select = "SELECT * FROM scrapp"
	mycursor.execute(sql_select)
	all_data = mycursor.fetchall()
	all_data_obj = []

	for y in all_data:

		all_data_obj.append({"image_url" : y[2], "job title" :  y[0], "company name" : y[1], "job url" : y[3], "job_release" : y[4]})

	return all_data_obj


#INSERTS ALL SCRAPPED DATA INTO DB
def insert_sql(job_obj):

	sql_insert = "INSERT INTO scrapp (job_title, company_name, job_image, job_url, job_release) VALUES (%s, %s, %s, %s, %s)"
	param = (job_obj["job title"], job_obj["company name"], job_obj["image_url"], job_obj["job url"], job_obj["job_release"])

	try:
		
		mycursor.execute(sql_insert, param)
		fulltien_dario.commit()
		print(mycursor.rowcount, 'JOB INSERTED.')
		
	except:
			
		print('THIS JOB IS ALREADY IN THE DATABASE.')