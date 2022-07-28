import smtplib
import datetime as dt
import random

MY_EMAIL = input("Enter your email and press enter: ")
MY_PASSWORD = input("Enter your password and press enter: ")

port = 587
receiver_email = "python_test@adminmytech.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=port) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=receiver_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
