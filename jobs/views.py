from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse, Http404
from jobs.models import Job
from notifications.models import Notification
from employees.forms import EmployeeForm
from django.urls import reverse

from .forms import JobForm

# Create your views here.
def create_job(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		job_form = JobForm(request.POST)
        # check whether it's valid:
		if job_form.is_valid():            
			# Create, but don't save the new job instance.
			new_job = job_form.save(commit=False)
			
			
			#Get current user
			user = request.user
			
			employer_name = user.employer.company_name
		
			# Add employer.
			new_job.employer = user.employer
			# Save the new instance.
			new_job.save()
			# redirect to a new URL:
			return HttpResponseRedirect(reverse('jobs:view'))

	# if a GET (or any other method) we'll create a blank form
	else:
		job_form = JobForm()
		
	user = request.user
			
	employer_name = user.employer.company_name
		
	return render(request, 'jobs/create_jobs.html', {'form': job_form,'company_name':employer_name})
	
	
def my_jobs(request):
	user = request.user			
	employer = user.employer
	
	#Get all jobs created by the current user
	jobs_list = Job.objects.filter(employer=employer).order_by('-created_on')
	return render(request, 'jobs/view_jobs.html', {'my_jobs': jobs_list,'company_name':employer.company_name})
	
def all_jobs(request):
	jobs_list = Job.objects.all()
	return render(request, 'jobs/jobs.html', {'jobs_list': jobs_list})
	
def apply_job(request, job_id):
	# if this is a POST request we need to process the form data
	job = get_object_or_404(Job, pk=job_id)
	
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		employee_form = EmployeeForm(request.POST,request.FILES)
        # check whether it's valid:
		if employee_form.is_valid():
            
			new_employee = employee_form.save(commit=False)			
			new_employee.job = job
			#new_employee.resume = request.FILES['resume']
			
			new_employee.save()
			
			#send email to employee
			new_employee.send_job_application_email(new_employee)
			
			#notify employer of new application
			message = new_employee.first_name+" has applied for "+job.title
			Notification.objects.create(message=message,employer=job.employer)
			
				
			# redirect to a new URL:
			return render(request,'jobs/application_successful.html',{'company_name': job.employer.company_name,"job_position":job.title})

    # if a GET (or any other method) we'll create a blank form
	else:
		employee_form = EmployeeForm()
		
	return render(request, 'jobs/apply_job.html', {'form': employee_form,'job':job})
	
	
def job_detail(request, job_id):
	# if this is a POST request we need to process the form data
	job = get_object_or_404(Job, pk=job_id)
		
	return render(request, 'jobs/job_details.html', {'job_item':job})

		
