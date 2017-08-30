from django.db import models
from django.db import models
from candidates.models  import Candidate

# Create your models here.
class Interview(models.Model):
	candidate = models.ForeignKey(Candidate, null=True, on_delete=models.CASCADE)
	interview_date = models.DateTimeField()
	
	
	def schedule_interview(self, candidate):
		candidate.is_shortlisted = True
		candidate.save()
		
		interview = Interview(candidate =self.candidate,interview_date=self.interview_date)	
		interview.save()
	 
