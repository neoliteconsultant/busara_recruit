from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Employee(models.Model):
	# user = models.OneToOneField(User, null=True)
	first_name  = models.CharField(blank=False, max_length=30,default="")
	last_name = models.CharField(blank=False, max_length=30,default="")
	username = models.CharField(blank=False, max_length=30,default="")
	password = models.CharField(blank=False, max_length=200,default="")
	email = models.CharField(blank=False, max_length=35,default="")
	phone_number = models.CharField(blank=True, max_length=12)
	#profile_photo = models.ImageField(upload_to='employees', blank=True)
	created_on = models.DateTimeField(auto_now=True)
	

@receiver(post_save, sender=User)
# function will be called after a user object is saved.
def create_employee(sender, instance, created, **kwargs):
	if created:
		Employee.objects.create(user=instance)