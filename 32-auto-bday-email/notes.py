# import smtplib
#
# my_email = "tbk81dev@gmail.com"
# password = "dnchhnyasyhcqwfb"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="tbk8181@yahoo.com",
#                         msg="Subject: First email\n\nHello world"
#                         )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1989, month=7, day=4)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

my_email = "tbk81dev@gmail.com"
password = "dnchhnyasyhcqwfb"

now = dt.datetime.now()
today = now.weekday()

if today == 0:
    with open("quotes.txt") as qt:
        lines = qt.readlines()
    q_of_week = random.choice(lines)

    print(q_of_week)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="tbk8181@yahoo.com",
                            msg=f"Subject: Your quote of the week\n\n{q_of_week}"
                            )

