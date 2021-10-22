
from django.contrib.auth.models import User

from django.db import models
from .threads import EmailThread


# Create your models here.
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(blank=False, unique=True, max_length=30)
    company_website = models.URLField(blank=False, unique=True, max_length=100)
    phone_number = models.CharField(blank=True, unique=True, max_length=12)
    company_logo = models.ImageField(upload_to='employers', blank=True, default="")
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.user.first_name + ' ' + self.user.last_name

    # Send email asychronously
    def send_signup_email(self, subject):
        email_thread = EmailThread(self.user.first_name, subject, self.user.email)
        email_thread.start()


