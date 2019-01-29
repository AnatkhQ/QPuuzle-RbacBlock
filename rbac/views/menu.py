#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import OrderedDict
from django.shortcuts import render, redirect, HttpResponse
from django.forms import formset_factory
from django.conf import settings
from django.utils.module_loading import import_string

from rbac import models
from rbac.forms.menu import MenuModelForm, SecondMenuModelForm, PermissionModelForm, MultiAddPermissionForm, \
    MultiEditPermissionForm
from rbac.service.urls import memory_reverse
from rbac.service.routes import get_all_url_dict


def menu_list(request):
    """
    菜单和权限列表
    :param request:
    :return:
    """

    menus = models.Menu.objects.all()
    menu_id = request.GET.get('mid')  # 用户选择的一级菜单
    second_menu_id = request.GET.get('sid')  # 用户选择的二级菜单

    menu_exists = models.Menu.objects.filter(id=menu_id).exists()

    if not menu_exists:  # 1.先判断是否存在这个id对应的一级菜单
        menu_id = None
    if menu_id:  # 2.如果有这个菜单，且有html有mid，则加载一级菜单对应的二级菜单
        second_menus = models.Permission.objects.filter(menu_id=menu_id)
    else:  # 3.如果url没有mid,则不展示二级菜单页面
        second_menus = []

    # 4.判断是否有id = second_menu_id的二级菜单，判断方法和一级菜单如初一则
    second_menu_exists = models.Permission.objects.filter(id=second_menu_id).exists()
    if not second_menu_exists:
        second_menu_id = None

    if second_menu_id:  # 5.如果有二级菜单ID，则展示权限列表
        permissions = models.Permission.objects.filter(pid_id=second_menu_id)
    else:
        permissions = []

    return render(
        request,
        'rbac/menu_list.html',
        {
            'menus': menus,
            'second_menus': second_menus,
            'permissions': permissions,
            'menu_id': menu_id,
            'second_menu_id': second_menu_id,
        }
    )


def menu_add(request):
    """
    添加一级菜单
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = MenuModelForm()
        return render(request, 'rbac/menu_change.html', {'form': form})

    form = MenuModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/menu_change.html', {'form': form})


def menu_edit(request, pk):
    """
    编辑一级菜单
    :param request:
    :param pk:
    :return:
    """
    obj = models.Menu.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('菜单不存在')
    if request.method == 'GET':
        form = MenuModelForm(instance=obj)
        return render(request, 'rbac/menu_change.html', {'form': form})

    form = MenuModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/menu_change.html', {'form': form})


def menu_del(request, pk):
    """
    删除一级菜单
    :param request:
    :param pk:
    :return:
    """
    url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Menu.objects.filter(id=pk).delete()
    return redirect(url)


def second_menu_add(request, menu_id):
    """
    添加二级菜单
    :param request:
    :param menu_id: 已选择的一级菜单ID（用于设置默认值）
    :return:
    """

    menu_object = models.Menu.objects.filter(id=menu_id).first()

    if request.method == 'GET':
        form = SecondMenuModelForm(initial={'menu': menu_object})
        return render(request, 'rbac/change.html', {'form': form})

    form = SecondMenuModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def second_menu_edit(request, pk):
    """
    编辑二级菜单
    :param request:
    :param pk: 当前要编辑的二级菜单
    :return:
    """

    permission_object = models.Permission.objects.filter(id=pk).first()

    if request.method == 'GET':
        form = SecondMenuModelForm(instance=permission_object)
        return render(request, 'rbac/change.html', {'form': form})

    form = SecondMenuModelForm(data=request.POST, instance=permission_object)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def second_menu_del(request, pk):
    """
    删除二级菜单
    :param request:
    :param pk:
    :return:
    """
    url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(id=pk).delete()
    return redirect(url)


def permission_add(request, second_menu_id):
    """
    添加权限
    :param request:
    :param second_menu_id:
    :return:
    """
    if request.method == 'GET':
        form = PermissionModelForm()
        return render(request, 'rbac/change.html', {'form': form})

    form = PermissionModelForm(data=request.POST)
    if form.is_valid():
        second_menu_object = models.Permission.objects.filter(id=second_menu_id).first()
        if not second_menu_object:  # 如果有二级菜单的对象，即为了防止用户手动修改url导致二级菜单出错
            return HttpResponse('二级菜单不存在，请重新选择！')
        form.instance.pid = second_menu_object
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def permission_edit(request, pk):
    """
    编辑权限
    :param request:
    :param pk: 当前要编辑的权限ID
    :return:
    """

    permission_object = models.Permission.objects.filter(id=pk).first()

    if request.method == 'GET':
        form = PermissionModelForm(instance=permission_object)
        return render(request, 'rbac/change.html', {'form': form})

    form = PermissionModelForm(data=request.POST, instance=permission_object)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def permission_del(request, pk):
    """
    删除权限
    :param request:
    :param pk:
    :return:
    """
    url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(id=pk).delete()
    return redirect(url)


def multi_permissions(request):
    """
    批量操作权限
    :param request:
    :return:
    """
    post_type = request.GET.get('type')  # 用于区别前端不同的post命令
    generate_formset_class = formset_factory(MultiAddPermissionForm, extra=0)
    update_formset_class = formset_factory(MultiEditPermissionForm, extra=0)

    generate_formset = None
    update_formset = None
    if request.method == 'POST' and post_type == 'generate':
        # 批量添加
        formset = generate_formset_class(data=request.POST)
        if formset.is_valid():
            object_list = []
            post_row_list = formset.cleaned_data

            has_error = False  # 判断是否有错误信息，用于判断只有全对才添加数据
            for i in range(0, formset.total_form_count()):  # 循环所有formset
                row_dict = post_row_list[i]
                if not row_dict:
                    continue
                try:
                    new_object = models.Permission(**row_dict)
                    new_object.validate_unique()  # 检查当前对象数据库是否存在唯一的异常.validate_unique()
                    object_list.append(new_object)
                except Exception as e:
                    formset.errors[i].update(e)
                    generate_formset = formset
                    has_error = True
            if not has_error:  # 没有错误信息
                models.Permission.objects.bulk_create(object_list, batch_size=100)  # 批量增加数据
        else:
            generate_formset = formset

    if request.method == 'POST' and post_type == 'update':
        # 批量更新
        formset = update_formset_class(data=request.POST)
        if formset.is_valid():
            post_row_list = formset.cleaned_data
            for i in range(0, formset.total_form_count()):
                row_dict = post_row_list[i]
                permission_id = row_dict.pop('id')
                try:
                    row_object = models.Permission.objects.filter(id=permission_id).first()
                    for k, v in row_dict.items():
                        setattr(row_object, k, v)
                    row_object.validate_unique()
                    row_object.save()
                except Exception as e:
                    formset.errors[i].update(e)
                    update_formset = formset
        else:
            update_formset = formset

    # 1. 获取项目中所有的URL
    all_url_dict = get_all_url_dict()
    """
    {
        'rbac:role_list':{'name': 'rbac:role_list', 'url': '/rbac/role/list/'},
        'rbac:role_add':{'name': 'rbac:role_add', 'url': '/rbac/role/add/'},
        ....
    }
    """
    router_name_set = set(all_url_dict.keys())  # 拿到路由系统中去重后的name集合
    # 2. 获取数据库中所有的URL
    permissions = models.Permission.objects.all().values('id', 'title', 'name', 'url', 'menu_id', 'pid_id')
    permission_dict = OrderedDict()
    permission_name_set = set()  # 拿到数据库中去重后的name
    for row in permissions:
        permission_dict[row['name']] = row
        permission_name_set.add(row['name'])  # 把name添加到集合中
    """
    {
        'rbac:role_list': {'id':1,'title':'角色列表',name:'rbac:role_list',url.....},
        'rbac:role_add': {'id':1,'title':'添加角色',name:'rbac:role_add',url.....},
        ...
    }
    """

    # 2.1数据库和路由系统中都存在的路由，判断相同的name是否url进行修改后不同
    for name, value in permission_dict.items():
        router_row_dict = all_url_dict.get(name)
        if not router_row_dict:
            continue
        if value['url'] != router_row_dict['url']:
            value['url'] = '路由和数据库中不一致'

    # 3. 应该添加、删除、修改的权限有哪些？
    # 3.1 计算出应该增加的name
    if not generate_formset:
        generate_name_list = router_name_set - permission_name_set
        generate_formset = generate_formset_class(
            initial=[row_dict for name, row_dict in all_url_dict.items() if
                     name in generate_name_list])

    # 3.2 计算出应该删除的name
    delete_name_list = permission_name_set - router_name_set
    delete_row_list = [row_dict for name, row_dict in permission_dict.items() if name in delete_name_list]

    # 3.3 计算出应该更新的name
    if not update_formset:
        update_name_list = permission_name_set & router_name_set
        update_formset = update_formset_class(
            initial=[row_dict for name, row_dict in permission_dict.items() if name in update_name_list])

    return render(
        request,
        'rbac/multi_permissions.html',
        {
            'generate_formset': generate_formset,
            'delete_row_list': delete_row_list,
            'update_formset': update_formset,
        }
    )


def multi_permissions_del(request, pk):
    """
    批量页面的权限删除
    :param request:
    :param pk:
    :return:
    """
    url = memory_reverse(request, 'rbac:multi_permissions')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(id=pk).delete()
    return redirect(url)


def distribute_permissions(request):
    """
    权限分配
    :param request:
    :return:
    """

    user_id = request.GET.get('uid')  # 拿到选中的用户uid
    # 业务中的用户表 "users.models.UserInfo""
    user_model_class = import_string(settings.RBAC_USER_MODLE_CLASS)

    user_object = user_model_class.objects.filter(id=user_id).first()
    if not user_object:
        user_id = None

    role_id = request.GET.get('rid')  # 拿到所选的角色
    role_object = models.Role.objects.filter(id=role_id).first()
    if not role_object:
        role_id = None

    if request.method == 'POST' and request.POST.get('type') == 'role':  # 由前端隐藏字段type:role进行form表单的区分
        role_id_list = request.POST.getlist('roles')
        if not user_object:
            return HttpResponse('请选择用户，然后再分配角色！')
        user_object.roles.set(role_id_list)

    if request.method == 'POST' and request.POST.get('type') == 'permission':
        permission_id_list = request.POST.getlist('permissions')
        print(permission_id_list)
        if not role_object:
            return HttpResponse('请选择角色，然后再分配权限！')
        role_object.permissions.set(permission_id_list)

    if user_id:
        user_has_roles = user_object.roles.all()
    else:
        user_has_roles = []

    user_has_roles_dict = {item.id: None for item in user_has_roles}

    # 获取当前用户的所有权限

    # 如果选中的角色，优先显示选中角色所拥有的权限
    # 如果没有选择角色，才显示用户所拥有的权限
    if role_object:  # 选择了角色
        user_has_permissions = role_object.permissions.all()
        user_has_permissions_dict = {item.id: None for item in user_has_permissions}

    elif user_object:  # 未选择角色，但选择了用户
        user_has_permissions = user_object.roles.filter(permissions__id__isnull=False).values('id',
                                                                                              'permissions').distinct()
        user_has_permissions_dict = {item['permissions']: None for item in user_has_permissions}
    else:
        user_has_permissions_dict = {}

    all_user_list = user_model_class.objects.all()

    all_role_list = models.Role.objects.all()

    # 所有的菜单（一级菜单）
    all_menu_list = models.Menu.objects.values('id', 'title')

    all_menu_dict = {}

    for item in all_menu_list:
        item['children'] = []
        all_menu_dict[item['id']] = item

    # 所有二级菜单
    all_second_menu_list = models.Permission.objects.filter(menu__isnull=False).values('id', 'title', 'menu_id')

    all_second_menu_dict = {}

    for row in all_second_menu_list:
        row['children'] = []
        all_second_menu_dict[row['id']] = row

        menu_id = row['menu_id']
        all_menu_dict[menu_id]['children'].append(row)

    # 所有三级菜单（不能做菜单的权限）
    all_permission_list = models.Permission.objects.filter(menu__isnull=True).values('id', 'title', 'pid_id')

    for row in all_permission_list:
        pid = row['pid_id']
        if not pid:  # 没有pid则找不到该权限的二级菜单
            continue
        all_second_menu_dict[pid]['children'].append(row)

    """
    [
        {
            id:1,
            title:'业务管理'
            children:[
                {
                    'id':11, 
                    title:'账单列表',
                    children:[
                        {'id':12,title:'添加账单'}
                    ]
                },
                {'id':11, title:'客户列表'},
            ]
        },
        
    ]
    """

    return render(
        request,
        'rbac/distribute_permissions.html',
        {
            'user_list': all_user_list,
            'role_list': all_role_list,
            'all_menu_list': all_menu_list,
            'user_id': user_id,
            'role_id': role_id,
            'user_has_roles_dict': user_has_roles_dict,
            'user_has_permissions_dict': user_has_permissions_dict,
        }
    )
