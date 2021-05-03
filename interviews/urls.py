from django.conf.urls import url

from . import views

app_name = 'interviews'  # namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
    url(r'^schedule/([0-9]+)/$', views.schedule_interview, name="schedule"),
    url(r'^view/$', views.my_interviews, name="view"),

]
