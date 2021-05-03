from django.db import models

from employers.models import Employer


# Create your models here.
class Notification(models.Model):
    employer = models.ForeignKey(Employer, null=True, on_delete=models.CASCADE)
    message = models.CharField(blank=False, max_length=150)
    created_on = models.DateTimeField(auto_now=True)
