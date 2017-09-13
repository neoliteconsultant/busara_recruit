from django.test import TestCase
from django.urls import reverse
from unittest import skip

from jobs.models import Job
from employers.models  import Employer 
from django.test import TestCase, RequestFactory

from .views import create_job

from django.contrib.auth.models import User
from django.http import HttpRequest

class JobTestCase(TestCase):

	@classmethod
	def setUpClass(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username="ann", email="ann@gmail.com",password="1234")		

		self.employer = Employer.objects.create(user=self.user,company_name="Quartz Accountants",company_website="https://www.quartz.io",phone_number="245711300900")
		
		

	
	#Test for job creation
	#@skip("Don't want to test")
	@skip("Don't want to test")
	def test_create_job(self):
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
		#self.assertRedirects(response, '/jobs/view/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
		self.assertEqual(response.status_code, 200)

		
		
	#Test for sucessful job application
	@skip("Don't want to test")
	def test_apply_job(self):
		"""Test for successful job application"""
		username= "lmuka"
		email= "lmuka@gmail.com"
		password = "1234"
		
		#, kwargs={'username':username,'password':password}
		
		response = self.client.post(reverse('employers:login'),{'username':username,'password':password})
		#self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Invalid credentials.")
		#self.assertRedirects(response, reverse('employers:dashboard'))
        
		
	
	
		

	