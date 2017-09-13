from django.test import TestCase

def test_home(self):
	response = self.client.get("/")
	self.assertTemplateUsed(r, 'home/index.html')

