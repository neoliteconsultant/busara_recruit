from django.db import models

from employers.models import Employer


# Create your models here.
class Job(models.Model):
    INDUSTRIES = (
        ('Any', 'Any'),
        ('Accounting', 'Accounting'),
        ('Customer Service', 'Customer Service'),
        ('Government', 'Government'),
        ('Education', 'Education'),
        ('Engineering', 'Engineering'),
        ('Hospitality', 'Hospitality'),
        ('Healthcare', 'Healthcare'),
        ('Farming and Agriculture', 'Farming and Agriculture'),
        ('IT and Telecoms', 'IT and Telecoms'),
        ('Legal', 'Legal'),
        ('Security', 'Security'),
        ('Other', 'Other'),
    )
    AVAILABILITY = (
        ('Fulltime', 'Fulltime'),
        ('Part time', 'Part time'),
    )
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=80, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    requirements = models.CharField(max_length=12000, default='')  # large max_length to accomodate storage of html text
    benefits = models.CharField(max_length=200, null=True, blank=True)
    industry = models.CharField(max_length=30, choices=INDUSTRIES, default=INDUSTRIES[0][0])
    availability = models.CharField(max_length=30, choices=AVAILABILITY, default=AVAILABILITY[0][0])
    location = models.CharField(max_length=100, default='')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
