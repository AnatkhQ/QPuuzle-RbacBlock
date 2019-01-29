#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf import settings


def init_permission(current_user, request):
    """
    用户权限的初始化
    :param current_user: 当前用户对象
    :param request: 请求相关所有数据
    :return:
    """
    # 2. 权限信息初始化
    # 根据当前用户信息获取此用户所拥有的所有权限，并放入session。
    # 根据角色获取所有权限
    # permissions__id__isnull=False为了防止新增加了职位，但是没有数据为null，需要对该数据进行排除
    # distinct()防止同一个用户有多个职位，多个职位有相同的权限，而出现重复数据，需要进行去重处理
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                                      "permissions__title",
                                                                                      "permissions__url",
                                                                                      "permissions__name",
                                                                                      "permissions__pid_id",
                                                                                      "permissions__pid__title",
                                                                                      "permissions__pid__url",
                                                                                      "permissions__menu_id",
                                                                                      "permissions__menu__title",
                                                                                      "permissions__menu__icon"
                                                                                      ).distinct()

    # 3. 获取权限+菜单信息
    permission_dict = {}

    menu_dict = {}

    for item in permission_queryset:
        ###### 处理权限 ######
        permission_dict[item['permissions__name']] = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url'],
            'pid': item['permissions__pid_id'],
            'p_title': item['permissions__pid__title'],
            'p_url': item['permissions__pid__url'],
        }

        ###### 处理菜单 ######
        menu_id = item['permissions__menu_id']  # 拿到menu_id用于确认1级菜单
        if not menu_id:
            continue

        # menu_id有值，则该权限为menu_id的1级菜单所属的2级菜单
        node = {'id': item['permissions__id'],
                'title': item['permissions__title'],
                'url': item['permissions__url']}

        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }

    # 将权限信息和菜单信息 放入session
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict
