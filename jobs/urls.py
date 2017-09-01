from django.conf.urls import url

from . import views
app_name = 'jobs' #namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
	url(r'^create/$', views.create_job, name="create"),
	url(r'^view/$', views.my_jobs, name="view"),
   

]