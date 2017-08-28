from django.db import models
from employers.models  import Employer 

# Create your models here.
class Job(models.Model):
	title = models.CharField(blank=False, max_length=30)
	employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
	requirements = models.CharField(max_length=1000,default='')
	created_on = models.DateTimeField(auto_now=True)
