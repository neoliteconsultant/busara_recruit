import os

from django.shortcuts import render,get_object_or_404
from employees.models import Employee
from jobs.models import Job

from django.conf import settings
from django.http import HttpResponse

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

# Create your views here.
#Get candidate profile
def candidate_profile(request,id):
	user = request.user			
	employer = user.employer
	
	profile = get_object_or_404(Employee, pk=id)
	return render(request, 'employees/view_profile.html', {'profile': profile,'company_name':employer.company_name})
	
def download(request, file_name):
	file_path = os.path.join(settings.MEDIA_ROOT, file_name)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			#response = HttpResponse(fh.read(), content_type="application/pdf")
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404