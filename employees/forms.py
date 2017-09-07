from django import forms
from django.forms import ModelForm, Textarea,TextInput, ClearableFileInput
from employees.models  import Employee

class EmployeeForm(ModelForm):
		class Meta:
			model = Employee
			exclude = ['job','application_date','is_shortlisted']
			widgets = {
			'first_name': TextInput(attrs={'class': 'form-control','placeholder':"First name"}),
			'last_name': TextInput(attrs={'class': 'form-control','placeholder':"Last name"}),
			'email': TextInput(attrs={'class': 'form-control','placeholder':"Email address"}),
			'phone_number': TextInput(attrs={'class': 'form-control','placeholder':"Phone number"}),
			'address': TextInput(attrs={'class': 'form-control','placeholder':"Address"}),
			'cover_letter': Textarea(attrs={'class': 'form-control','cols': 6, 'rows': 5,'placeholder':"Cover letter"}),
			'resume': ClearableFileInput(attrs={'accept': '.doc,.pdf'}),
			}
			
