from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from employers.models  import Employer 
from django.conf import settings


# Create your views here.
def index(request):
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
	
		employer = Employer(first_name=first_name,last_name=last_name,username=username, email=email, password=password,company_name=company_name,company_website=company_website,phone_number=phone_number)
		employer.save()
		
		# employer.send_signup_email('Activate your Busara recruit account')
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		#return HttpResponseRedirect(reverse('employers:registration_success', args=(email,)))
		return HttpResponseRedirect(reverse('employers:registration_success', args=(email,)))
		
    

def login(request):
    return render(request,'employers/login.html')

def logout(request):
    return HttpResponse("You're logging out an employer.")
	
	
def registration_success(request, email):
    return HttpResponse("Confirm your email address\nAn email from Busara recruit has been sent to " % email %	
	" please follow instructions in the emails to finish setting up your account")