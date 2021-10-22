
from django.db import models
from .threads import JobApplicationThread

from jobs.models import Job


# Employee/Job Applicant/Candidate.
class Employee(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(blank=False, max_length=30, default="")
    last_name = models.CharField(blank=False, max_length=30, default="")
    email = models.EmailField(blank=False, max_length=35, default="")
    phone_number = models.CharField(blank=False, max_length=12)
    address = models.CharField(blank=True, max_length=60)
    cover_letter = models.CharField(max_length=17000, default='')  # large max_length to accomodate storage of html text
    resume = models.FileField(upload_to='resume/%Y%m%d/', default='')
    application_date = models.DateTimeField(auto_now=True)
    is_shortlisted = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name + ' ' + self.last_name

    # Send email asychronously
    def send_job_application_email(self, employee):
        email_thread = JobApplicationThread(employee)
        email_thread.start()



