from django.db import models
from employees.models  import Employee
from jobs.models  import Job

# Create your models here.
class Candidate(models.Model):
	title = models.CharField(blank=False, max_length=30)
	job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
	# file will be saved to MEDIA_ROOT/cover_letters/2015/01/30
	cover_letter = models.FileField(upload_to='cover_letters/%Y/%m/%d/',default='')
	resume = models.FileField(upload_to='resume/%Y/%m/%d/',default='')
	application_date = models.DateTimeField(auto_now=True)
	is_shortlisted = models.BooleanField(default=False)
