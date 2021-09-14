import multiprocessing
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if(re.fullmatch(regex, email)):
        return email
    else:
        if re.fullmatch(regex, email[:len(email)]):
            return email[:len(email)]

        else:
            return None

def mailit(mails, file):

    fromaddr = "contrivers512@gmail.com"
    toaddr = mails
    msg = MIMEMultipart()
    msg['From'] = "Contrivers Events contrivers512@gmail.com"
    msg['To'] = toaddr
    msg['Subject'] = "Join the India's Biggest Designathon"
    f = open("../mail.html")
    body = f.read()
    f.close()
    msg.attach(MIMEText(body, 'html'))
    filename = "designathon.docx"
    attachment = open(file, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)


# print(type(sys.argv[-1]))


def collector(data):
    for i in data:
        for k in data[i][:-1]:
            path = i.replace(' ', '') + ".docx"
            if check(k):
                mailit(k, f"../docs/{path}")
        print("done!!!")


if __name__ == "__main__":
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("contrivers512@gmail.com", "sahil@shuvam2003")
    print("logged In")
    from websites import school, distributor

    num_process = 1
    lst = distributor(school, num_process)
    processes = []
    for i in lst:
        p = multiprocessing.Process(target=collector, args=[i])
        p.start()
        processes.append(p)
    for i in processes:
        i.join()

    s.quit()
    print("logged Out")
