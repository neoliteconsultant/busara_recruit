import unittest
from django.core import mail
from django.conf import settings
from .mailer import Mailer

class MailerTestCase(unittest.TestCase):
	
	def test_send_email(self):
			# Send message.
			mail.send_mail(
            'Subject here', 'Here is the message.',
            settings.EMAIL_HOST_USER, ['tonyafula@gmail.com'],
            fail_silently=False,
			)

			# Test that one message has been sent.
			self.assertEqual(len(mail.outbox), 1)

			# Verify that the subject of the first message is correct.
			self.assertEqual(mail.outbox[0].subject, 'Subject here')