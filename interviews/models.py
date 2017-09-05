from django.db import models
from django.db import models
from employees.models  import Employee
from jobs.models  import Job

# Create your models here.
class Interview(models.Model):
	employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
	interview_type = models.CharField(max_length=60,blank=False,default='')
	location = models.CharField(max_length=60,blank=False,default='')
	#message = models.CharField(max_length=300,blank=False,default='')
	interview_date = models.DateTimeField()
	

