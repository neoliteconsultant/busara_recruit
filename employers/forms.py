from django import forms
from jobs.models  import Job
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea,TextInput,ChoiceField
from employers.models import Employer

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
	password = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Password'}))
	
class RegisterForm(forms.Form):
	#company_logo = forms.ImageField()
	first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First name'}))
	last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))
	username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
	email = forms.EmailField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
	phone_number = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Phone number'}))
	company_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Company name'}))
	company_website = forms.URLField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Company website'}))
	password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password'}))
	password_confirmation = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm password'}))
	
	
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
	
class SignUpForm(ModelForm):
		class Meta:
			model = Employer
			exclude = ['created_on']
			widgets = {
			'phone_number': TextInput(attrs={'class': 'form-control'}),
			'company_name': forms.Select(attrs={'class': 'form-control'}),
			'company_website': TextInput(attrs={'class': 'form-control'}),
			}
	
	
