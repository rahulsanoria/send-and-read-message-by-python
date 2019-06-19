import smtplib


server = smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()
server.login('rahul.kumar25011999@gmail.com', '07sainty')

message  = 'Hi There , sending message from Python'
server.sendmail('rahul.kumar25011999@gmail.com' , 'clanclash675@gmail.com')
server.quit()
