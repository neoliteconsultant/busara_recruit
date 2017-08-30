from django.db import models
from employers.models  import Employer 

# Create your models here.
class Job(models.Model):
	title = models.CharField(blank=False, max_length=30)
	employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
	requirements = models.CharField(max_length=1000,default='')
	created_on = models.DateTimeField(auto_now=True)
	
	def __str__(self): # __unicode__ on Python 2
		return self.title
	
	def create_job(self, employer):
		job = Job(title=self.title, employer=self.employer,requirements=self.requirements)
		job.save()
		
	def get_job(self, job_id):
		job = Job.objects.get(pk=job_id)
		return job
		
	def get_all_jobs(self):
		jobs = Job.objects.all()
		return jobs
		
	
