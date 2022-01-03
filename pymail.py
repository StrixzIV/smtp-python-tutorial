import smtplib
import imghdr
from email.message import EmailMessage

msg = EmailMessage()

msg['subject'] = 'Never gonna give you up'
msg['From'] = 'sender@gmail.com'
msg['To'] = 'reciver@gmail.com'

with open('image.jpg', 'rb') as image:
    fname = image.name
    ftype = imghdr.what(image)
    fdata = image.read()

msg.set_content('Never gonna let you down. Never gonna run around and desert you.')
msg.add_attachment(fdata, maintype = 'image', subtype = ftype, filename = fname)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('sender@gmail.com', 'password')
    smtp.send_message(msg)