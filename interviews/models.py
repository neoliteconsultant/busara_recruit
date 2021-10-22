
from django.db import models
from .threads import InterviewThread

from employees.models import Employee


# Create your models here.
class Interview(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    interview_type = models.CharField(max_length=60, blank=False, default='')
    location = models.CharField(max_length=60, blank=False, default='')
    # message = models.CharField(max_length=300,blank=False,default='')
    interview_date = models.DateTimeField()

    # Send email asychronously
    def send_interview_email(self, interview):
        email_thread = InterviewThread(interview)
        email_thread.start()


