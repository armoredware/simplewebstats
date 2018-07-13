import smtplib

sender = 'mmd4@westchestergov.com'
receiver = 'mmd4@westchestergov.com'
subject = 'Test Subject'
content = """This is an e-mail message to be sent in HTML format
<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""


message = 'From: From Person <'+sender+'>To: To Person <'+receiver+""">
MIME-Version: 1.0
Content-type: text/html
Subject:"""+subject+"""

"""+content

try:
   smtpObj = smtplib.SMTP('smtp2.westchestergov.com', 25) 
   #server.set_debuglevel(1)
   smtpObj.sendmail(sender, receiver, message)
   print ("Successfully sent email")
except:
   print ("Error: unable to send email ")