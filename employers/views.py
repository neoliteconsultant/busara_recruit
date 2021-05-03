from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from employees.models import Employee
from employers.models import Employer
from jobs.models import Job
from notifications.models import Notification
from .forms import SignUpForm


# Create your views here.
def index(request):
    return render(request, 'employers/index.html')


def dashboard(request):
    try:
        # Get logged in user object
        if request.user.is_authenticated:
            employer = request.user.employer
            employer_name = employer.company_name

            notifications = Notification.objects.filter(employer=employer).order_by('-created_on')
            jobs = Job.objects.filter(employer=employer)
            total_jobs = jobs.count()

            # Get all candidate who have applied for job belonging to this user
            # Order by application_date descending
            total_candidates = Employee.objects.filter(job__in=jobs).count()
            shortlisted_candidates = Employee.objects.filter(job__in=jobs, is_shortlisted=True).count()

            return render(request, 'employers/index.html',
                          {'company_name': employer_name, 'notifications': notifications, 'total_jobs': total_jobs,
                           'total_candidates': total_candidates, 'shortlisted_candidates': shortlisted_candidates})
        else:
            return render(request, 'employers/login.html')
    except Employer.DoesNotExist:
        return render(request, 'employers/login.html', {'error_message': "Username does not exist."})


def register(request):
    if request.method == 'GET':
        return render(request, 'employers/register.html')

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

        try:
            if password != password_confirmation:
                return render(request, 'employers/register.html', {'error_message': "Passwords do not match."})
            else:

                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                employer = Employer(user=user, company_name=company_name, company_website=company_website,
                                    phone_number=phone_number)
                employer.save()

                employer.send_signup_email('Activate your Busara recruit account')
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('employers:email_confirmation', args=(email,)))
        except IntegrityError as e:
            return render(request, 'employers/register.html', {'error_message': e.__cause__})


def register2(request):
    register_form = SignUpForm(request.POST)
    return render(request, 'employers/register.html', {'form': register_form})


def login_employer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('employers:dashboard'))
        else:
            return render(request, 'employers/login.html', {'error_message': "Invalid credentials."})


    else:
        return render(request, 'employers/login.html')


def logout_employer(request):
    logout(request)
    return render(request, 'employers/login.html')


def email_confirmation(request, email):
    return render(request, 'employers/register_successful.html', {'email': email})
