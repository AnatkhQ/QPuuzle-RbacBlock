#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import reverse
from django.http import QueryDict


def memory_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的URL（替代了模板中的url）
    :param request:
    :param name: 反向生成URL的name
    :return:
    """
    basic_url = reverse(name, args=args, kwargs=kwargs)

    
    if not request.GET:
        return basic_url

    query_dict = QueryDict(mutable=True)
    query_dict['_filter'] = request.GET.urlencode()  # mid=2&age=99

    return "%s?%s" % (basic_url, query_dict.urlencode())


def memory_reverse(request, name, *args, **kwargs):
    """
    反向生成URL
        http://127.0.0.1:8001/rbac/menu/add/?_filter=mid%3D2
        1. 在url中讲原来搜索条件，如filter后的值
        2. reverse生成原来的URL，如：/menu/list/
        3. /menu/list/?mid%3D2
    """
    url = reverse(name, args=args, kwargs=kwargs)
    origin_params = request.GET.get('_filter')
    if origin_params:
        url = "%s?%s" % (url, origin_params,)

    return url
