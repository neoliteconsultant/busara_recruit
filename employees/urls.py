from django.conf.urls import url

from . import views
app_name = 'candidates' #namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
	url(r'^view/$', views.my_candidates, name="view"),
   

]