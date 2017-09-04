from django.test import TestCase
from django.urls import reverse
from unittest import skip

from employers.models import Employer
from django.contrib.auth.models import User

class EmployerTestCase(TestCase):

	
	#Test for sign up
	#@skip("Don't want to test")
	def test_sign_up(self):
		"""Test for successful employer sign_up"""
		first_name = "Lisa"
		last_name = "Muka"
		email = "lmuka@gmail.com"
		username = "lmuka"
		password = "1234"		
		password_confirmation = "1234"		
		company_name = "Lorex Pharmaceuticals"
		company_website = "http://www.lorex.com"
		phone_number = "254788190774"
	
		
		message = """Confirm your email address\nAn email from Busara recruit has been sent to lmuka@gmail.com	
		 please follow instructions in the emails to finish setting up your account"""
		
		response = self.client.post(reverse('employers:register'), {'first_name':first_name,'last_name':last_name,'email':email,'username':username,'password':password,'password_confirmation':password_confirmation,'company_name':company_name,'company_website':company_website,'phone_number':phone_number})
		
		#self.assertEqual(response.status_code, 200)
		self.assertRedirects(response, '/employers/email_confirmation/'+email, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
		#self.assertContains(response, message)
		
		
	#Test for sucessful sign in
	@skip("Don't want to test")
	def test_sign_in(self):
		"""Test for successful employer sign_in"""
		username= "lmuka"
		email= "lmuka@gmail.com"
		password = "1234"
		
		#, kwargs={'username':username,'password':password}
		
		response = self.client.post(reverse('employers:login'),{'username':username,'password':password})
		#self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Invalid credentials.")
		#self.assertRedirects(response, reverse('employers:dashboard'))
        
		
	
	#Test for unsucessful sign in
	def test_sign_in_unsucessful(self):
		"""Test for unsuccessful employer sign_in"""
		
		response = self.client.post(reverse('employers:login'),{'username':"biriani",'password':"loboso"})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Invalid credentials.")
		

	