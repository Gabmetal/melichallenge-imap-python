import imaplib
import email
import mysql.connector
from dateutil.parser import parse
from os import environ
import datetime

mydb = mysql.connector.connect(
  host=environ['MYSQL_HOST'],
  user=environ['MYSQL_USER'],
  passwd=environ['MYSQL_PASSWORD'],
  database=environ['MYSQL_DB']
)

mail = imaplib.IMAP4_SSL(environ['EMAIL_HOST'])
mail.login(environ['EMAIL_USER'],environ['EMAIL_PASSWORD'])
mail.select('inbox')

def fetch():
	print ("Start Fetching")
	rv, data = mail.search(None, 'ALL')
	if rv != 'OK':
		print ("No message found")
		return
	for num in data[0].split():
		rv, data = mail.fetch(num, '(RFC822)')
		if rv != 'OK':
			print("ERROR getting message", num)
			return
		msg = email.message_from_bytes(data[0][1])
		hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
		
		date_tuple = email.utils.parsedate_tz(msg['date'])
		if date_tuple:
			email_date = datetime.datetime.fromtimestamp(
				email.utils.mktime_tz(date_tuple))
			
		email_from = str(email.header.make_header(email.header.decode_header(msg['from'])))
		email_subject = str(hdr)
		mycursor = mydb.cursor()
		
		if (("DevOps" in email_subject) or ("DevOps" in msg.get_payload())):
			sql = "INSERT INTO email_devops (fecha, `from`, subject) VALUES (%s, %s, %s);"
			val = (email_date, email_from, email_subject)
			mycursor.execute(sql, val)
			mydb.commit()
			print(mycursor.rowcount, "record inserted.")
			
fetch()