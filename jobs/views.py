from django.shortcuts import render
from django.http import HttpResponseRedirect
from jobs.models import Job

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
	

		
