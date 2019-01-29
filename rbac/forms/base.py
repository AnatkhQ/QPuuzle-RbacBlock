#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms


class BootStrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BootStrapModelForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
