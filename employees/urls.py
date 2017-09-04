from django.conf.urls import url

from . import views
app_name = 'candidates' #namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
	url(r'^view/$', views.my_candidates, name="view"),
	url(r'^profile/(?P<id>[0-9]+)$', views.candidate_profile, name="profile"),
	url(r'^download/(?P<file_name>.+)$', views.download, name="download")
   

]