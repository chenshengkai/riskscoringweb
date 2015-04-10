# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django import forms
from forms import UserCreateForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.shortcuts import redirect
from models import BaseInfo, BaseInfoImporterModel
from django.contrib.auth.models import User
from data_importer.views import DataImporterForm
from data_importer.tasks import DataImpoterTask
from forms import BaseCreateForm

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/importinfo/")
    else:
        form = UserCreateForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, context_instance=RequestContext(request))

def index(request):
	return HttpResponse("请输入用户的基本信息")

class import_create_view(DataImporterForm):
    extra_context = {'title': '请导入用户基本信息:',
                         'template_file': 'importinfo/base_info.xlsx'}
    template_name = "importinfo/import.html"
    success_url = '../list_base'
    importer = BaseInfoImporterModel
    def form_valid(self, form, owner=None):
        return super(import_create_view, self).form_valid(form)


class BaseInfoListView(ListView):
    model = BaseInfo
    template_name = 'importinfo/baseinfo_list.html'
    def get_queryset(self):
        return BaseInfo.objects.filter(create_by=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(BaseInfoListView, self).get_context_data(**kwargs)
        return context

class BaseInfoDetailView(DetailView):
    model = BaseInfo
    template_name = 'importinfo/base_detail.html'
    slug_field = 'customer_id'
    slug_url_kwarg = 'cust'
    def get_context_data(self, **kwargs):
        context = super(BaseInfoDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
class BaseInfoCreateView(CreateView):
    form_class = BaseCreateForm
    template_name = 'importinfo/create.html'
    success_url = '/importinfo/list_base/'
    def render_to_response(self, context, **response_kwargs):
        if self.request.user.id is None:
            return redirect('/importinfo/login')
        return super(BaseInfoCreateView, self).render_to_response(context, **response_kwargs)
# Create your views here.
