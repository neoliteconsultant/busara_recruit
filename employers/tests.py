from django.test import TestCase
from employers.models import Employer

class EmployerTestCase(TestCase):
	#Test for sign up
	def test_sign_up(self):
		"""Test for successful employer sign up"""
		new_employer = Employer(first_name="Lorraine",last_name="Muka",username="lmuka", email="lmuka@gmail.com", password = "1234",company_name="Lorex Pharmaceuticals",phone_number="254788190774",address="AirtelHouse")
		new_employer.sign_up()
		#self.assertEqual(new_employer.sign_up(), 1)
	
	

	