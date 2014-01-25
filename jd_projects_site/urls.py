from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url, static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = []
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'jd_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^projects/', include('jd_projects.urls'))
)

