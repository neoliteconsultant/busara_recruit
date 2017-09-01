from django.db import models
from django.db import models
from employees.models  import Employee

# Create your models here.
class Interview(models.Model):
	employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
	interview_date = models.DateTimeField()
	
	
	def schedule_interview(self, employee):
		employee.is_shortlisted = True
		employee.save()
		
		interview = Interview(employee =self.employee,interview_date=self.interview_date)	
		interview.save()
	 
