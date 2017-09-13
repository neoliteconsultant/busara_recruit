from django.test import TestCase
from django.urls import reverse
from unittest import skip

from jobs.models import Job
from employers.models  import Employer 
from django.test import TestCase, RequestFactory

from .views import create_job,apply_job

from django.contrib.auth.models import User
from django.http import HttpRequest

class JobTestCase(TestCase):


	@classmethod
	def setUpTestData(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username="ann", email="ann@gmail.com",password="1234")		

		self.employer = Employer.objects.create(user=self.user,company_name="Quartz Accountants",company_website="https://www.quartz.io",phone_number="245711300900")
		
		

	
	#Test for job creation
	#@skip("Don't want to test")
	def test_successful_job_creation(self):
		"""Test for successful job creation"""
		
		title ="Accountant"
		industry ="Accounting"
		location ="Thika Rd"
		availability="Part time"
		description="Maintain books of account"
		requirements="CPA 6/Bsc Business Administration"
		benefits="Health Insurance"
		
		# Create an instance of a POST request.
		request = self.factory.post('/jobs/create',{'employer':self.employer,'title':title,'industry':industry,'location':location,'availability':availability,'description':description,'requirements':requirements,'benefits':benefits})
		
		# Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
		request.user = self.user
		
		response = create_job(request)
		self.assertEqual(response.status_code, 302)
		

		
		
	#Test for sucessful job application
	@skip("Don't want to test")
	def test_apply_job(self):
		"""Test for successful job application"""
		job = Job.objects.create(employer=self.employer,title="Sr. Backend developer",industry="IT and Telecoms",location="Nairobi, Kenya",availability="Part time",description="IT Guru",requirements="Bsc Computer Science")
		
		request.user = self.user
		
		response = apply_job(request,job.id)
		self.assertEqual(response.status_code, 302)
        
		
	
	
		

	