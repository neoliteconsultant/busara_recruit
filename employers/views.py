from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from employers.models  import Employer 
from django.conf import settings

from . forms import LoginForm
from .forms import RegisterForm, SignUpForm


# Create your views here.
def index(request):
    return render(request,'employers/index.html')
	
def dashboard(request):
	#Get logged in user object
	if request.user.is_authenticated:
		employer = request.user.employer
		employer_name = employer.company_name
		
		return render(request,'employers/index.html',{'company_name':employer_name})
	else:
		return render(request,'employers/login.html')
	
def register(request):		
	if request.method == 'POST':
		#register_form = RegisterForm(request.POST,request.FILES)
		register_form = RegisterForm(request.POST)
		# check whether it's valid:
		if register_form.is_valid():  
			first_name = register_form.cleaned_data['first_name']
			last_name = register_form.cleaned_data['last_name']
			username = register_form.cleaned_data['username']
			email = register_form.cleaned_data['email']
			phone_number = register_form.cleaned_data['phone_number']
			company_name = register_form.cleaned_data['company_name']
			company_website = register_form.cleaned_data['company_website']
			password = register_form.cleaned_data['password']
			password_confirmation = register_form.cleaned_data['password_confirmation']
			
		
		    
			user = User.objects.create_user(username, email,password)		
			user.first_name=first_name
			user.last_name=last_name
			user.save()
			
			#company_logo=request.FILES['company_logo']
			employer = Employer(user=user,company_name=company_name,company_website=company_website,phone_number=phone_number)
			employer.save()
		
			
			employer.send_signup_email('Activate your Busara recruit account')
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return HttpResponseRedirect(reverse('employers:email_confirmation', args=(email,)))
		
			
	else:
		register_form = RegisterForm(request.POST)
		
	return render(request,'employers/register.html',{'form': register_form})
		
		
def register2(request):
	register_form = SignUpForm(request.POST)
	return render(request,'employers/register.html',{'form': register_form})
    

def login_employer(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		#employer = Employer.objects.get(username=username,password=password)
		user = authenticate(request,username=username, password=password)
		
		if user is not None:
			login(request, user)
			# redirect to a new URL:
			return HttpResponseRedirect(reverse('employers:dashboard'))
		else:
			return render(request,'employers/login.html',{'error_message': "Invalid credentials."})
	
	
	else:	
		return render(request,'employers/login.html')

def logout_employer(request):
		logout(request)
		return render(request,'employers/login.html')
	
def email_confirmation(request, email):
    return render(request,'employers/register_successful',{'email': email})