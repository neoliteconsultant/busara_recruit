import threading
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class JobApplicationThread(threading.Thread):
    """ Email thread for sending an email when
        an employee makes an application"""
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