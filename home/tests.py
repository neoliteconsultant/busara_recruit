from django.test import TestCase
from django.urls import reverse
from jobs.models import Job


def test_all_jobs(self):
	response = self.client.get(reverse('home:job_listing'))
	self.assertQuerysetEqual(response.context['jobs_list'],[])

