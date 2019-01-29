#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from rbac import models


class RoleModelForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ['title', ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '请输入角色名称', 'class': 'form-control'})
        }

