import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import get_template

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


# Email thread for sending an email when
# an employee makes an application
class JobApplicationThread(threading.Thread):
    def __init__(self, employee):
        threading.Thread.__init__(self)
        self.employee = employee

    def run(self):
        html_template = get_template('employees/email/job_application.html')
        plaintext_template = get_template('employees/email/job_application.txt')

        job_title = self.employee.job.title
        company_name = self.employee.job.employer.company_name
        candidate_email = self.employee.email
        candidate_name = self.employee.first_name + ' ' + self.employee.last_name

        params = {'job_title': job_title,
                  'company_name': company_name, 'candidate_name': candidate_name, 'candidate_email': candidate_email,
                  "candidate_phone": self.employee.phone_number, "candidate_address": self.employee.address,
                  "cover_letter":
                      self.employee.cover_letter}

        text_content = plaintext_template.render(params)
        html_content = html_template.render(params)

        subject = "Job Application for " + job_title

        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [candidate_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=True)
