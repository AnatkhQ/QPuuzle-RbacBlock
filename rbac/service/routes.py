#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string

# Django1.*只需导入以下模块
from django.urls import RegexURLResolver, RegexURLPattern  # Django1.*  urlpatterns类型


# Django2.* 需要导入以下模块
# from django.urls import URLResolver, URLPattern  # Django2.* urlpatterns类型
# from pro_crm import urls  # Django2.* 获取项目全部URL，需要获取根urlpatterns


def check_url_exclude(url):
    """
    自定制排除一些特定的URL
    :param url:
    :return:
    """
    for regex in settings.AUTO_DISCOVER_EXCLUDE:
        if re.match(regex, url):  # 如果在白名单内的URL，则不需要进行全局URL展示
            return True


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    """
    递归的去获取URL
    :param pre_namespace: namespace前缀，以后用户拼接name
    :param pre_url: url前缀，以后用于拼接url
    :param urlpatterns: 路由关系列表
    :param url_ordered_dict: 用于保存递归中获取的所有路由
    :return:
    """
    for item in urlpatterns:
        if isinstance(item, RegexURLPattern):  # 非路由分发，将路由添加到url_ordered_dict
            if not item.name:  # 如果没有name则无法添加到全局URL内
                continue

            if pre_namespace:
                name = "%s:%s" % (pre_namespace, item.name)
            else:
                name = item.name

            ######### Django1.* 获取regex路径方法 item._regex获取当前URL前缀 #########
            url = pre_url + item._regex  # /^rbac/^user/edit/(?P<pk>\d+)$/

            ######### Django2.* 获取regex路径方法 item.pattern.regex.pattern#########
            # url = pre_url + item.pattern.regex.pattern  # /rbac/user/edit/(?P<pk>\d+)/

            url = url.replace('^', '').replace('$', '')  # 去除正则匹配符号

            if check_url_exclude(url):  # 如果是白名单的路由，则不需要匹配出来
                continue

            url_ordered_dict[name] = {'name': name, 'url': url}

        elif isinstance(item, RegexURLResolver):  # 路由分发，递归操作

            if pre_namespace:
                if item.namespace:
                    namespace = "%s:%s" % (pre_namespace, item.namespace,)
                else:
                    namespace = item.namespace
            else:
                if item.namespace:
                    namespace = item.namespace
                else:
                    namespace = None
            ######### Django1.* 有两种获取获取正则路径的方式#########
            # 递归进入更深层的include路由，第二个参数前缀的URL需要把上一层的URL和这一层的URL加起来
            # 方法一：
            recursion_urls(namespace, pre_url + item.regex.pattern, item.url_patterns, url_ordered_dict)
            # 方法二：
            # recursion_urls(namespace, pre_url + item._regex, item.url_patterns, url_ordered_dict)

            ######### Django2.* #########
            # recursion_urls(namespace, pre_url + item.pattern.regex.pattern, item.url_patterns, url_ordered_dict)


def get_all_url_dict():
    """
    获取项目中所有的URL（必须有name别名）
    :return:
    """
    url_ordered_dict = OrderedDict()

    ##### Django1.*使用import_string获取urlpatterns #####
    md = import_string(settings.ROOT_URLCONF)  # from luff.. import urls  获取到项目根路由ROOT_URLCONF
    recursion_urls(None, '/', md.urlpatterns, url_ordered_dict)  # 递归去获取所有的路由，根路由前缀namespace为None，默认URL路径前缀为/

    ##### Django2.*需导入urlpatterns获取 #####
    # print(urls.urlpatterns)
    # recursion_urls(None, '/', urls.urlpatterns, url_ordered_dict)  # 递归去获取所有的路由

    return url_ordered_dict
