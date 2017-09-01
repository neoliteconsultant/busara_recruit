from django.shortcuts import render
from employees.models import Employee
from jobs.models import Job

# Create your views here.
#Get all candidates who applied for jobs belonging to the current user
def my_candidates(request):
	user = request.user			
	employer = user.employer	
	
	jobs = Job.objects.filter(employer=employer)
	#Get all candidate who have applied for job belonging to this user
	#Order by application_date descending
	candidate_list = Employee.objects.filter(job__in=jobs).order_by('-application_date')
	return render(request, 'employees/view_candidates.html', {'candidate_list': candidate_list,'company_name':employer.company_name})
