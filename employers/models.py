from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.
class Employer(models.Model):
	#user = models.OneToOneField(User, null=True)
	first_name  = models.CharField(blank=False, max_length=30,default='')
	last_name = models.CharField(blank=False, max_length=30,default='')
	username = models.CharField(blank=False, max_length=30,default='')
	password = models.CharField(blank=False, max_length=20,default='')
	email = models.CharField(blank=False, max_length=35,default='')
	company_name = models.CharField(blank=False, max_length=200,default='')
	phone_number = models.CharField(blank=True, max_length=12)
	address = models.CharField(blank=True, max_length=100)
	company_logo = models.ImageField(upload_to='employers', blank=True)
	created_on = models.DateTimeField()
	
	
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
@receiver(post_save, sender=User)
# function will be called after a user object is saved.
def create_employer(sender, instance, created, **kwargs):
    if created:
        Employer.objects.create(user=instance)
# 		
def sign_up(self,first_name,last_name,username, email, password,company_name,phone_number,address):		
	employer = Employer(first_name=first_name,last_name=last_name,username=username, email=email, password=password,company_name=company_name,phone_number=phone_number,address=address)
	employer.save()
	
# def login(self,username,password):	
	

# def logout(self,username,password):


	
	