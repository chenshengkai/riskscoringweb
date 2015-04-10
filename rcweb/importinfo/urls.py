# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from importinfo import views
from importinfo.models import BaseInfo, BaseInfoImporterModel
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', views.register, name='register'),
    url(r'^create/$', views.BaseInfoCreateView.as_view(), name="create_base"),
    url(r'^import/$', views.import_create_view.as_view(), name="import"),
    url(r'^list_base/$', views.BaseInfoListView.as_view(), name='list_base'),
#    url(r'^uploadbureau/(?P<custid>[-_\w]+)/$',views.upload_bureau_view.as_view(), name='uploadbureau'),
    url(r'^detail_base/(?P<cust>[-_\w]+)/$', views.BaseInfoDetailView.as_view(), name = 'detail_base'),
)