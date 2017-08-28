from django.db import models
from django.db import models
from jobs.models  import Job

# Create your models here.
class Interview(models.Model):
	job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
	interview_date = models.DateTimeField(auto_now=True)
