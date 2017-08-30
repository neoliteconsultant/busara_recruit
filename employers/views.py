from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from employers.models  import Employer 
from django.conf import settings

from . forms import LoginForm


# Create your views here.
def index(request):
    return render(request,'employers/index.html')
	
def dashboard(request):
    return render(request,'employers/index.html')
	
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
		
		
		
		if password == password_confirmation:
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
		else:
			return render(request,'employers/register.html',{'error_message': "Passwords do not match."})
    

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
    return HttpResponse("Confirm your email address\nAn email from Busara recruit has been sent to " + email +	
	" please follow instructions in the emails to finish setting up your account")