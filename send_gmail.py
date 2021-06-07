import smtplib
import html_email
from email.message import EmailMessage

#SENDS MAIL FUNCTION
def envia_mail(job_obj):
	msg = EmailMessage()
	msg['From'] = "your_gmail" 
	msg['To'] = "recep_gmail" 
	msg['Subject'] = "Mail subject"
	msg.set_content('job')
	msg.add_alternative(html_email.html_gmail(job_obj), subtype='html')
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(msg['From'],'your_password')

	try:
		
		server.send_message(msg)
				
	except:
		
		print('ERROR: MAIL HAS NOT BEEN SENT')