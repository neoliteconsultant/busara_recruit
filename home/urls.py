from django.conf.urls import url

from . import views
app_name = 'home'

urlpatterns = [
    url(r'^$', views.home),
	url(r'^home/$', views.home, name="home"),
    url(r'^job_listing/$', views.all_jobs, name ="job_listing"),
	url(r'^apply_job/(?P<job_id>[0-9]+)$', views.apply_job, name ="apply_job"),
	#url(r'^(?P<question_id>[0-9]+)/$', views.apply_job, name='applyjob'),
	
]