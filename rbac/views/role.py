#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
角色管理
"""
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from rbac import models
from rbac.forms.role import RoleModelForm
from django.views.decorators.csrf import csrf_exempt


def role_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    role_queryset = models.Role.objects.all()

    return render(request, 'rbac/role_list.html', {'roles': role_queryset})


def role_add(request):
    """
    添加角色
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = RoleModelForm()
        return render(request, 'rbac/change.html', {'form': form})

    form = RoleModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/change.html', {'form': form})


def role_edit(request, pk):
    """
    编辑角色
    :param request:
    :param pk: 要修改的角色ID
    :return:
    """
    obj = models.Role.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('角色不存在')
    if request.method == 'GET':
        form = RoleModelForm(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})

    form = RoleModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/change.html', {'form': form})


# 跳转删除需要修改url接收pk
# def role_del(request, pk):
#     """
#     删除角色
#     :param request:
#     :param pk:
#     :return:
#     """
#     origin_url = reverse('rbac:role_list')
#     if request.method == 'GET':
#         return render(request, 'rbac/delete.html', {'cancel': origin_url})
#
#     models.Role.objects.filter(id=pk).delete()
#     return redirect(origin_url)

# 弹出框删除使用该函数，并且修改此函数的url为不接收pk
@csrf_exempt
def role_del(request):
    """
    删除角色v2.0
    :return:
    """
    status = {"msg": None}
    pk = request.POST.get("pk")
    print(pk)
    if pk:
        models.Role.objects.filter(id=pk).delete()
        status["msg"] = True
    else:
        return render(request, "rbac/error-404.html")

    return JsonResponse(status)
