import  smtplib

my_email = "python_test@adminmytech.com"
password = "f7JjCRqYyy"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="hudspeth199@yahoo.com", msg="Python Email!!")
connection.close()
