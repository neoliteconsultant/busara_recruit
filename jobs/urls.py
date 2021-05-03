from django.conf.urls import url

from . import views

app_name = 'jobs'  # namespacing prevents conflicts when there are multiples views with same name in different apps

urlpatterns = [
    url(r'^$', views.all_jobs),
    url(r'^create/$', views.create_job, name="create"),
    url(r'^view/$', views.my_jobs, name="view"),
    url(r'^job_listing/$', views.all_jobs, name="job_listing"),
    url(r'^apply/(?P<job_id>[0-9]+)$', views.apply_job, name="apply"),
    url(r'^detail/(?P<job_id>[0-9]+)$', views.job_detail, name="detail"),

]
