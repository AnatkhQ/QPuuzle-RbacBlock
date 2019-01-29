#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from rbac import models


class UserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        """
        检测密码是否一致
        :return:
        """
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码输入不一致')
        return confirm_password


class UpdateUserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'email', ]

    def __init__(self, *args, **kwargs):
        super(UpdateUserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ResetPasswordUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(ResetPasswordUserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        """
        检测密码是否一致
        :return:
        """
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('两次密码输入不一致')
        return confirm_password
