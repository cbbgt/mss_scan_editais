
import requests


def send_email(subject, body):
    email_to_send = 'ctoledo@pieracciani.com.br'
    response = requests.post('https://us-central1-emailsender-352520.cloudfunctions.net/gmailSender', json=[
        {
            'MIMEMultipart': False,
            'Subject': subject,
            'To': email_to_send,
            'Body': body
        }
    ])
