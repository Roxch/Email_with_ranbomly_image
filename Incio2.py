
import smtplib, ssl
import os
import getpass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randrange

#Searches a folder full of images for a random image.
def Imagen():
	#All images are listed.
	ListOfFolder = os.listdir('tokyocyb0rg')

	#Get the number of files with Len (only tells me the items in listFolder).
	NumberOfFiles = len(ListOfFolder)
	NumberOfFiles += 1

	#Random number.
	r = randrange(0, NumberOfFiles)
	Imagen = ListOfFolder[r]
	#Returns Image which is an <str> of the image file name.
	return(Imagen)

#For the Subject to have a different name each time it is sent.
def NumRanCode():
	Code = randrange(1000, 9999)
	return(Code)

#Sender = Emisor | Receiver = Receptor
UserSender = input('Your Email : ')
PASSWORD = getpass.getpass('password plis : ')
UserReceiver = input('Email of your friend : ')

mens_email ='''<!DOCTYPE html>
<html>
  <body>
	<center><p>Hello User of the Wired</p></center>
	<center><img src="cid:image1"></center>
	<center><p>:D</p></center>
  </body>
</html>

'''

CodeSpam = NumRanCode()
message = MIMEMultipart('related')
message['Subject'] = f'({CodeSpam}) WIRED ({CodeSpam})'
message['From'] = UserSender
message['To'] = UserReceiver

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

msgAlternative.attach(MIMEText(mens_email, 'html', 'utf-8'))

img = Imagen()

fp = open(f'tokyocyb0rg/{img}', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

#created conection segured
context = ssl.create_default_context()

try :
	Server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
	Server.login(UserSender, PASSWORD)
	Server.sendmail(UserSender, UserReceiver, message.as_string())
	#success = exito
	print('¡Success!')
except smtplib.SMTPException :
	#bad = mal
	print('¡Bad!')