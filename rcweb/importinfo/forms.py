# -*- coding: UTF-8 -*-
__author__ = 'Michael'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import NON_FIELD_ERRORS
from models import BaseInfo

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.RegexField(label="用户名:", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=("**必填. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class BaseCreateForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = BaseInfo
        exclude = ("customer_id", "create_by", "insert_date", "scoring_status")
        help_texts ={
            'customer_name':'申请人姓名',
            'annual_income':'(必填)申请人的年收入单位元',
            'education':'(必填)',
            'property':'(必填)',
            'marriage':'(必填)',
            'position':'(必填)',
            'nature':'(必填)',
            'creditcard_quota':'(必填)',
            }
        widgets = {
            'property_location': forms.TextInput(attrs={'size':50}),
            'company_name':forms.TextInput(attrs={'size':30}),
            'loan_purpose':forms.TextInput(attrs={'size':50}),
            'company_address':forms.TextInput(attrs={'size':50}),
            'residence_year': forms.NumberInput(attrs={'size':20}),
            'residential_address': forms.TextInput(attrs={'size':50}),
            'residence_address': forms.TextInput(attrs={'size':50}),
        }
        error_messages = {'education': {'required': '下面这项内容为必填!'},
                          'loan_purpose': {'required': '下面这项内容为必填!'},
                          'property': {'required': '下面这项内容为必填!'},
                          'nature': {'required': '下面这项内容为必填!'},
                          'position': {'required': '下面这项内容为必填!'},}
