import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class InterviewThread(threading.Thread):
    """
    Email thread for sending an email when
    an employee is invited for an interview
    """
    def __init__(self, interview):
        threading.Thread.__init__(self)
        self.interview = interview

    def run(self):
        html_template = get_template('interviews/email/interview_invitation.html')
        plaintext_template = get_template('interviews/email/interview_invitation.txt')

        job_title = self.interview.employee.job.title
        company_name = self.interview.employee.job.employer.company_name
        interview_type = self.interview.interview_type

        params = {'username': self.interview.employee.first_name, 'job_title': job_title,
                  'company_name': company_name, 'interview_type': interview_type, 'location': self.interview.location,
                  "interview_date": self.interview.interview_date}

        text_content = plaintext_template.render(params)
        html_content = html_template.render(params)

        subject = interview_type + " @ " + company_name
        recipient_email = self.interview.employee.email

        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [recipient_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=True)

