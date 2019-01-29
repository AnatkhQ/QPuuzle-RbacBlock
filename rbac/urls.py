#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from rbac.views import role
from rbac.views import user
from rbac.views import menu

urlpatterns = [

    url(r'^role/list/$', role.role_list, name='role_list'),  # rbac:role_list
    url(r'^role/add/$', role.role_add, name='role_add'),  # rbac:role_add
    url(r'^role/edit/(?P<pk>\d+)/$', role.role_edit, name='role_edit'),  # rbac:role_edit
    # 跳转式删除
    # url(r'^role/del/(?P<pk>\d+)/$', role.role_del, name='role_del'),  # rbac:role_del
    # 弹出框删除
    url(r'^role/del/$', role.role_del, name='role_del'),  # rbac:role_del

    # url(r'^user/list/$', user.user_list, name='user_list'),
    # url(r'^user/add/$', user.user_add, name='user_add'),
    # url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),  # rbac:user_edit
    # url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
    # url(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),

    url(r'^menu/list/$', menu.menu_list, name='menu_list'),
    url(r'^menu/add/$', menu.menu_add, name='menu_add'),
    url(r'^menu/edit/(?P<pk>\d+)/$', menu.menu_edit, name='menu_edit'),
    url(r'^menu/del/(?P<pk>\d+)/$', menu.menu_del, name='menu_del'),

    url(r'^second/menu/add/(?P<menu_id>\d+)$', menu.second_menu_add, name='second_menu_add'),
    url(r'^second/menu/edit/(?P<pk>\d+)/$', menu.second_menu_edit, name='second_menu_edit'),
    url(r'^second/menu/del/(?P<pk>\d+)/$', menu.second_menu_del, name='second_menu_del'),

    url(r'^permission/add/(?P<second_menu_id>\d+)/$', menu.permission_add, name='permission_add'),
    url(r'^permission/edit/(?P<pk>\d+)/$', menu.permission_edit, name='permission_edit'),
    url(r'^permission/del/(?P<pk>\d+)/$', menu.permission_del, name='permission_del'),

    url(r'^multi/permissions/$', menu.multi_permissions, name='multi_permissions'),
    url(r'^multi/permissions/del/(?P<pk>\d+)/$', menu.multi_permissions_del, name='multi_permissions_del'),

    url(r'^distribute/permissions/$', menu.distribute_permissions, name='distribute_permissions'),

]
