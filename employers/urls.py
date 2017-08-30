from django.conf.urls import url

from . import views
app_name = 'employers' #namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
    url(r'^$', views.index),
	url(r'^login/$', views.login, name="login"),
	url(r'^employers/$', views.login),
    url(r'^register/$', views.register, name="register"),
	url(r'^registration_success/(\w)/$', views.registration_success, name="registration_success")

]