#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, reverse, redirect
from django.conf import settings


class RbacMiddleware(MiddlewareMixin):
    """
    用户权限信息校验
    """

    def process_request(self, request):
        """
        当用户请求刚进入时候执行
        :param request:
        :return:
        """

        """
        1. 获取当前用户请求的URL
        2. 获取当前用户在session中保存的权限列表 ['/customer/list/','/customer/list/(?P<cid>\\d+)/']
        3. 权限信息匹配（匹配路径这种有正则符号的字符串不能使用==，需要使用re.match(样本,比较的素材)进行正则匹配）
        """

        # 1.白名单中的URL无需权限验证即可访问
        current_url = request.path_info
        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url, current_url):
                return None

        # 2.获取当前用户权限列表
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_dict:
            return HttpResponse('未获取到用户权限信息，请登录！')
            # return redirect(reverse('login'))  # 可自行根据name进行反向生成

        # 3.定义路径导航格式
        url_record = [
            {'title': '首页', 'url': '#'}
        ]

        # 4.需要登录，但无需权限校验的URL
        for url in settings.NO_PERMISSION_LIST:
            if re.match(url, current_url):
                request.current_selected_permission = 0  # 给request注册一个全局属性：当前选中的URL，0为没有选中任何菜单URL
                request.breadcrumb = url_record  # 注册全局属性breadcrumb用来更方便获取路径导航数据url_record
                request.menu_name = '首页'  # 当前路径导航名称
                return None

        flag = False

        for item in permission_dict.values():
            reg = "^%s$" % item['url']  # 匹配URL的完整路径，防止出现多个匹配
            if re.match(reg, current_url):
                flag = True
                request.current_selected_permission = item['pid'] or item['id']  # 当前菜单选中的URL的id，如果有pid则为pid,没有pid则为id
                if not item['pid']:  # 没有pid，则为二级菜单
                    # extend列表，拼接该权限的路径导航，class:active选中该路径
                    url_record.extend([{'title': item['title'], 'url': item['url'], 'class': 'active'}])
                else:  # 有pid则为pid二级菜单所属的普通权限
                    url_record.extend([
                        {'title': item['p_title'], 'url': item['p_url']},  # 该权限对应的二级菜单
                        {'title': item['title'], 'url': item['url'], 'class': 'active'},
                    ])
                request.breadcrumb = url_record
                break

        # 获取路径导航对应的目录名
        for url in url_record:
            if "class" in url:
                request.menu_name = url.get("title")


        if not flag:  # 没有匹配的权限，则无权访问
            return HttpResponse('无权访问')  # 可进行自定制，例如返回404页面
