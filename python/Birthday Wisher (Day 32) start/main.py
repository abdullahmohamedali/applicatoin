import smtplib


my_email = "abdullah.khafagy2@gmail.com"
password ="smbu ltos hjuf dobu"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="nehadebeed@gmail.com", msg="hello")
connection.close()

