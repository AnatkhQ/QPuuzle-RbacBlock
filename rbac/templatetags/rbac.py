#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.template import Library
from django.conf import settings
from collections import OrderedDict
from rbac.service import urls

register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    """
    创建一级菜单
    :return:
    """
    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    """
    创建二级菜单
    :return:
    """

    # menu_dict是一个字典，使用menu_dict渲染menu会让模板变得无序
    # 需要使用有序字典，让menu每次都是固定的顺序
    menu_dict = request.session[settings.MENU_SESSION_KEY]

    key_list = sorted(menu_dict)

    ordered_dict = OrderedDict()

    for key in key_list:
        val = menu_dict[key]
        val['class'] = ''  # 默认每一个1级菜单不展开，隐藏二级菜单

        for per in val['children']:

            if per['id'] == request.current_selected_permission:  # 二级菜单ID = 当前选中菜单对应的ID/PID，用于判断展开哪个一级菜单
                per['class'] = 'active'
                val['class'] = 'nav-active'  # 让1级菜单的class由hide--->空
        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    """
    路径导航
    :param request:
    :return:
    """

    return {'record_list': request.breadcrumb, 'record_name': request.menu_name}


@register.filter
def has_permission(request, name):
    """
    判断是否有权限,register.filter最多可传2个参数
    {% request|has_permission:name %}
    :param request:
    :param name:
    :return:
    """
    if name in request.session[settings.PERMISSION_SESSION_KEY]:
        return True


@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的URL（替代了模板中的url）
    :param request:
    :param name:
    :return:
    """
    return urls.memory_url(request, name, *args, **kwargs)
