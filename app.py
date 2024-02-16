import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr

sender_name = 'your name'

sender_email = "your email"
# note app password is different from regular password
email_password = 'your email app password'

subject = "Application for Junior Developer Role."
pdf_file_path = 'C:\\Users\\New\\Downloads\\rohit_resume_cr.pdf'  # Replace with the actual path to your PDF file
pdf_name = 'rohit_resume'

with open('emails.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        email_send = line[0]
        company_name = line[1]
        # text = "hello " + line[1] + " your " + line[2] + " has been activated"

         # Your desired email template
        text = """
Dear HR Team,

I trust this email finds you well. My name is Rohit, I recently came across your company's profile on LinkedIn and was impressed by your work and achievements. I am writing to express my interest in potential opportunities for a Junior Python/Django Developer role at {company_name}. 

I have attached my resume for your reference, and you can also find more about my professional background on my resume. 

Thank you for your time and consideration. I look forward to hearing from you, and I welcome any decision you may reach.

Best regards   
Rohit J    
        """.format(company_name=company_name)

        # Set the sender's name and email address
        formatted_sender = formataddr((sender_name, sender_email))

        # Create the MIMEText object for the email body
        body = MIMEText(text, 'plain')

        # Create the MIMEMultipart object and set the headers
        msg = MIMEMultipart()
        msg['From'] = formatted_sender
        msg['To'] = email_send
        msg['Subject'] = subject

        # Attach the body to the MIMEMultipart object
        msg.attach(body)

        with open(pdf_file_path, 'rb') as attachment:
            part = MIMEBase('application', 'pdf')  # Change 'octet-stream' to 'pdf'
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'inline; filename={pdf_name}')  # Set to 'inline'

            msg.attach(part)

        # Establish a connection to the SMTP server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, email_password)
            server.sendmail(sender_email, [email_send], msg.as_string())
