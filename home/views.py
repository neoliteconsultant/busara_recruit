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
	

	
	
