import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "contrivers512@gmail.com"
# toaddr = "shuvamanupam7@gmail.com"
toaddr = "sahilku2003@gmail.com, contrivers512@gmail.com, shuvamanupam7@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = "Contrivers Events contrivers512@gmail.com"

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "The Real Final HTML"

# string to store the body of the mail
f = open("mail.html")
body = f.read()
f.close()

# attach the body with the msg instance
msg.attach(MIMEText(body, 'html'))

# open the file to be sent
filename = "design.pdf"
attachment = open("./design.pdf", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "sahil@shuvam2003")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
