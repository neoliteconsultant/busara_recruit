import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class EmailThread(threading.Thread):
    def __init__(self, username, subject, recipient_email):
        threading.Thread.__init__(self)
        self.username = username
        self.subject = subject
        self.recipient_email = recipient_email

    def run(self):
        html_template = get_template('employers/email/sign_up.html')
        plaintext_template = get_template('employers/email/sign_up.txt')

        params = {'username': self.username}

        text_content = plaintext_template.render(params)
        html_content = html_template.render(params)

        msg = EmailMultiAlternatives(self.subject, text_content, settings.EMAIL_HOST_USER, [self.recipient_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=True)
