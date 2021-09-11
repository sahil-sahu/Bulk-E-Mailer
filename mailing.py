import smtplib
from mail import send_mail

sender = "contrivers512@gmail.com"
psswd = "sahil@shuvam2003"
to = "sahilku2003@gmail.com"
sub = "Designathon"
content = "aloo"
file = ["./design.pdf"]
smtp = smtplib.SMTP("localhost", 587)
smtp.starttls()
smtp.login(sender, psswd)
send_mail(to, sub, content, file)
smtp.quit()
