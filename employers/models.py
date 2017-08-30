import threading
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


from django.conf import settings

# Create your models here.
class Employer(models.Model):
	user = models.OneToOneField(User, null=True)
	# first_name  = models.CharField(blank=False, max_length=30,default='')
	# last_name = models.CharField(blank=False, max_length=30,default='')
	# username = models.CharField(blank=False, unique=True, max_length=30,default='')
	# password = models.CharField(blank=False, unique=True, max_length=20,default='')
	# email = models.CharField(blank=False, unique=True, max_length=35,default='')
	company_name = models.CharField(blank=False,unique=True, max_length=30,default='')
	company_website = models.CharField(blank=False,unique=True, max_length=100,default='')
	phone_number = models.CharField(blank=True, unique=True, max_length=12)
	# company_logo = models.ImageField(upload_to='employers', blank=True)
	created_on = models.DateTimeField(auto_now=True)
	
	def __str__(self): # __unicode__ on Python 2
		return self.first_name+' '+self.last_name	
	
		
		
	#Send email asychronously	
	def send_signup_email(self,subject):
		email_thread = EmailThread(self.user.first_name,subject,self.user.email)
		email_thread.start()
		
class EmailThread(threading.Thread):
	def __init__(self, username, subject, recipient_email):
		threading.Thread.__init__(self)
		self.username = username
		self.subject = subject
		self.recipient_email = recipient_email
		
	def run(self):
		html_template = get_template('employers/email/sign_up_email_template.html')
		plaintext_template = get_template('employers/email/sign_up_email_template.txt')
		
		params = {'username': self.username }
		
		text_content = plaintext_template.render(params)
		html_content = html_template.render(params)
		
		msg = EmailMultiAlternatives(self.subject, text_content, settings.EMAIL_HOST_USER, [self.recipient_email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

	
	