import smtplib
import datetime as dt 
import random
import os

script_dir=os.path.dirname(__file__)
quote_path=os.path.join(script_dir,'quotes.txt')
connection=smtplib.SMTP("smtp.gmail.com")
my_email="aminucf2002@gmail.com"
my_password="aoso qrhh nhnd fnhb"
now=dt.datetime.now()
weekday=now.weekday()
if weekday ==2:
    file_path=os.path
    with open (quote_path) as quotes_file:
        all_quotes=quotes_file.readlines()
        quote=random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg=f"Subject:Hello\n\n{quote}")