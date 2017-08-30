from django.db import models
from employees.models  import Employee
from jobs.models  import Job

# Job applications
class Candidate(models.Model):
	title = models.CharField(blank=False, max_length=30)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee, null=True,on_delete=models.CASCADE)
	# file will be saved to MEDIA_ROOT/cover_letters/2015/01/30
	cover_letter = models.FileField(upload_to='cover_letters/%Y/%m/%d/',default='')
	resume = models.FileField(upload_to='resume/%Y/%m/%d/',default='')
	application_date = models.DateTimeField(auto_now=True)
	is_shortlisted = models.BooleanField(default=False)
	
	def __str__(self): # __unicode__ on Python 2
		return self.title
	
	#Create candidate
	def apply_job(self,job,employee):
		candidate = Candidate(title=self.title,employee=self.employee,cover_letter=self.cover_letter.url,resume=self.resume.url)
		candidate.save()
		
	def view_candidates(self,job):
		return Candidate.objects.filter(job=self.job)
		#return Candidate.objects.filter(job__id=self.job.id)
		
	def get_shortlisted_candidates(self,job):
		return Candidate.objects.filter(job=self.job,is_shortlisted=True)
