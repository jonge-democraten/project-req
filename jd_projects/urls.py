from django.conf.urls import patterns, include, url
from jd_projects.views import ProjectRequestView, RequestSuccessView

urlpatterns = patterns('', 
    url(r'^request/', RequestProjectView.as_view(), name="request_project"),
    url(r'^request_success/', RequestSuccessView.as_view(), name="request_success")
)
