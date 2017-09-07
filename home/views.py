from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from employees.forms import EmployeeForm
from jobs.models import Job
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request,'home/index.html')
	
def all_jobs(request):
	jobs_list = Job.objects.all()
	return render(request, 'home/jobs.html', {'jobs_list': jobs_list})
	
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
			
			#TODO:send email to employee
			#TODO: notify employer of new application
			new_employee.send_job_application_email(new_employee)
				
			# redirect to a new URL:
			return render(request,'home/application_successful.html',{'company_name': job.employer.company_name,"job_position":job.title})

    # if a GET (or any other method) we'll create a blank form
	else:
		employee_form = EmployeeForm()
		
	return render(request, 'home/apply_job.html', {'form': employee_form,'job':job})
	
	
