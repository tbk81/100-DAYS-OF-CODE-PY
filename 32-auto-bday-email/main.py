import smtplib

my_email = "tbk81dev@gmail.com"
password = "dnchhnyasyhcqwfb"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="tbk8181@yahoo.com", msg="Hello world")
connection.close()
