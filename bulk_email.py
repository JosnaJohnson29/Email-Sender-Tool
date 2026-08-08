import json

import pandas as pd
import smtplib

with open('config.json','r') as p:
    params = json.load(p)['params']

    
your_email = params["email"]
your_password = params["password"]


data = pd.read_excel("email.xlsx")  
#print(data.head())
emails = data['Emails'].values
#print(emails)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_email, your_password)

subject = "Test Email Two"
msg ="Hello How are you This is bulk email"
body = f"Subject: {subject}\n\n {msg}"

for email in emails:
    server.sendmail(your_email, email, body)
    
server.quit()
