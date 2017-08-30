from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


# Create your models here.
class Mailer:
	def __init__(self,subject,sender,message,recipient):
		self.subject = subject
		self.sender = sender
		self.message = message
		self.recipient = recipient

	def send_simple_email(self):
		send_mail(self.subject,self.message,
		settings.EMAIL_HOST_USER,[self.recipient],fail_silently=False)
		
	#Adapted from https://stackoverflow.com/questions/2809547/creating-email-templates-with-django	
	def send_signup_email(self, username,subject,recipient):
		html_template = get_template('mail_templates/sign_up.html')
		plaintext_template = get_template('mail_templates/sign_up.txt')
		d = Context({'username': username })

		
		text_content = plaintext_template.render(d)
		html_content = html_template.render(d)
		msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [recipient])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		

