# SMTP library 
import smtplib

# Enabling the program to format your email correctly.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Enabling time stamp.
import datetime

# Enabling us to read html file
import codecs

# Main function that handles sending emails via Outlook's smtp server.
## Warning!!! Please find out the correct server address and port number from
## your email service providers(e.g.: Gmail->smtp.gmail.com:587) before your try.
def sendEmail(from_addr, to_addr_list, cc_addr_list,
              subject, message, login, password,
              smtpServer='smtp-mail.outlook.com:587'):
    # header = 'From: %s' % from_addr
    # header += 'To: %s' % ', '.join(to_addr_list)
    # header += 'Cc: %s' % ', '.join(cc_addr_list)
    # header += 'Subject: %s' % subject
    # message = header + message
    nowStr = datetime.datetime.now().strftime("%a %d %b, %I:%M:%S%P")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject + ' ' + nowStr
    msg['From'] = fromAddress
    msg['To'] = toAddress
    text_body = MIMEText(message, 'html', 'utf-8')
    msg.attach(text_body)

    # setup a SMTP server with address and port number.
    print("1.Start to setup connection with the SMTP server: " + smtpServer)
    server = smtplib.SMTP(smtpServer)
    server.starttls()
    print("1.Connected to SMTP server!")

    # provide login info
    print("---Login in process---")
    server.login(login, password)
    print("---Login successfully!---")

    # Send the email.
    print("---Sending Email!---")
    problems = server.sendmail(from_addr, to_addr_list, msg.as_string())
    print("---Finish Sending Email!---")

    # print any error messages that may exists 
    print(problems)
    server.quit()

#<-----------------Start of Demo Area--------------->#
# provide basic info that you want to send.
fromAddress = "***@***.com" # Sender Email address.
toAddress = "***@***.com" # Receivers' Email address.
ccAddress = [] # doesnt work here.
Subject = "Python email"

# Please store the content you want to send into the "Email.html" file.
f = codecs.open("Email.html", 'r') 
msg_body = f.read()
print(msg_body)
f.close()

# Provide the name and password info that allow you login to the smtp server of your email services.
login_name = "***@***.com"
password = "******"

sendEmail(fromAddress, toAddress, ccAddress, Subject, msg_body, login_name, password)
#<-----------------End of Demo Area--------------->#



