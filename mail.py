import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mailit(mails, file):

    fromaddr = "contrivers512@gmail.com"
    toaddr = ", ".join(mails)

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = "Contrivers Events contrivers512@gmail.com"

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Designathon"

    # string to store the body of the mail
    f = open("mail.html")
    body = f.read()
    f.close()

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'html'))

    # open the file to be sent
    filename = "designathon.docx"
    attachment = open(file, "rb")

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

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("contrivers512@gmail.com", "sahil@shuvam2003")

for i in range(3):
    mailit(["sahilku2003@gmail.com", "shuvamanupam7@gmail.com",
            "contact.contrivers@gmail.com"], "./docs/KENDRIYAVIDYLAYAAFSBIDAR.docx")
    print("done!!!")

s.quit()
