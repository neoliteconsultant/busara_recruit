from django.conf.urls import url

from . import views
app_name = 'employers' #namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
    # url(r'^$', views.index),
	url(r'^dashboard/$', views.dashboard, name="dashboard"),
	url(r'^login/$', views.login_employer, name="login"),
    url(r'^register/$', views.register, name="register"),
	url(r'^email_confirmation/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', views.email_confirmation, name="email_confirmation")

]