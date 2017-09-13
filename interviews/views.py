from django.shortcuts import get_object_or_404,render
from employees.models import Employee
from interviews.models import Interview
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def schedule_interview(request,employee_id):
	user = request.user
	employer = user.employer
	employee = get_object_or_404(Employee, pk=employee_id)
	interviewee = employee
	
	# if this is a POST request we need to process the form data
	if request.method == 'POST':	
		job = employee.job
	
		interview_type = request.POST['interview_type']
		location = request.POST['location']
		interview_date = request.POST['interview_date']
		date_object = datetime.strptime(interview_date, '%m/%d/%Y %I:%M %p')
		formatted_date = date_object.strftime('%Y-%m-%d %H:%M')
		
		interview = Interview(employee=employee, interview_type = interview_type, location = location, interview_date=formatted_date)	
		interview.save()
		
		employee.is_shortlisted = True
		employee.save()
		
		interview.send_interview_email(interview)
		
		# redirect to a new URL:
		return HttpResponseRedirect(reverse('interviews:view'))
		
	else:
		return render(request, 'interviews/schedule_interview.html', {'company_name':employer.company_name,'interviewee':interviewee})
		
def my_interviews(request):
	user = request.user			
	employer = user.employer
	
	#jobs = Job.objects.filter(employer=employer)
	
	
	interviews = Interview.objects.all().order_by('-interview_date')
	return render(request, 'interviews/view_interviews.html', {'interviews': interviews,'company_name':employer.company_name})
	
