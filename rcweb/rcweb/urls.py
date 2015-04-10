from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rcweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^importinfo/', include('importinfo.urls', namespace="importinfo")),
    url(r'^admin/', include(admin.site.urls)),
)
