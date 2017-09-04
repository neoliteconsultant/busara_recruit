from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from employers.models  import Employer 
from django.conf import settings

from django.shortcuts import get_object_or_404

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
	if request.method == 'GET':
		return render(request,'employers/register.html')
		
	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		phone_number = request.POST['phone_number']
		company_name = request.POST['company_name']
		company_website = request.POST['company_website']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']
		
		
		if password != password_confirmation:
			return render(request,'employers/register.html',{'error_message': "Passwords do not match."})
		else:		
			user = User.objects.create_user(username, email,password)		
			user.first_name=first_name
			user.last_name=last_name
			user.save()
			
			employer = Employer(user=user,company_name=company_name,company_website=company_website,phone_number=phone_number)
			employer.save()
		
			
			employer.send_signup_email('Activate your Busara recruit account')
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return HttpResponseRedirect(reverse('employers:email_confirmation', args=(email,)))
			
		
		
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
    return render(request,'employers/register_successful.html',{'email': email})