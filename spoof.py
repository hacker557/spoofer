import smtplib

from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.sendgrid.net'  # smtp.mail.yahoo.com

smtp_ssl_port = 465

username = 'apikey'

password = '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'

sender = 'kavyach997@gmail.com'

targets = ['jagarlamudisumithra@gmail.com', 'kasireddyvenkateswarlu@protonmail.com']

msg = MIMEText('Hi, how are you today?')

msg['Subject'] = 'Hello'

msg['From'] = sender

msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

server.login(username, password)

server.sendmail(sender, targets, msg.as_string())

server.quit()
