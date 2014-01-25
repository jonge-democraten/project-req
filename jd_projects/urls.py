from django.conf.urls import patterns, include, url
from jd_projects.views import RequestProjectView

urlpatterns = patterns('', 
    url(r'^request/', RequestProjectView.as_view(), name="request_project")
)
