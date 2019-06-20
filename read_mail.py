import email
import imaplib


username = 'your_email_id'
password = 'your_password'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)

mail.select('inbox')

mail.list()

result , data = mail.uid('search' , None  , 'ALL')

inbox_item_list = data[0].split()

most_recent = inbox_item_list[-1]

oldest = inbox_item_list[0]

result2 , email_data = mail.uid('fetch' , most_recent , '(RFC822)')

raw_email = email_data[0][1]

email_message = email.message_from_string(raw_email)

email_message['To']
email_message['From']
email_message['Subject']
email_message.get_payload()


  
# message = MIMEText(message_text)
# message['to'] = to
# message['from'] = sender
# message['subject'] = subject

# def __str__(self):
# 	return {'raw': base64.urlsafe_b64encode(message.as_string())}
