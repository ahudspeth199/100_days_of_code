import smtplib, ssl

my_email = input("Enter your email and press enter: ")
password = input("Enter your password and press enter: ")
message = "Python Email!!"
port = 587
receiver_email = "python_test@adminmytech.com"

context = ssl.create_default_context()

with smtplib.SMTP("smtp.mail.yahoo.com", port=port) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg="Subject: Email from Python\n\nTrying to send a quote"
    )


