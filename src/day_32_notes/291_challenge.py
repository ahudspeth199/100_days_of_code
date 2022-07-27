import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
        with open("quotes.txt",'r') as quotes:
            lines = quotes.read().splitlines()
            q_message = random.choice(lines)

        import smtplib, ssl

        my_email = input("Enter your email and press enter: ")
        password = input("Enter your password and press enter: ")
        message = q_message
        port = 587
        receiver_email = "python_test@adminmytech.com"

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_email,
                msg=f"Subject: Email from Python\n\nTrying to send a quotes {q_message}"
            )





# The open() function returns a file object which you will use to read text from a text file

        #lines = quotes.read()
        #print(lines)
        #myline = random.choice(lines)
        #print(myline)


# The open() function returns a file object which is an iterable object.
# Therefore, you can use a for loop to iterate over the lines of a text file
        """
        for line in quotes:
            print(line)
        """
# how to use the read() to read the text file line by line:
        """
        while True:
            lines = quotes.read()
            if not lines:
                break
            print(lines)
        """

# How to create a list of all the lines inside a particular text file



