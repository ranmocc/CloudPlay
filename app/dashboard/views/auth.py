# coding:utf-8
from django.views.generic import View
from django.shortcuts import redirect,reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth

class Login(View):
    TEMPLATE = '/dashboard/auth/login.html'
    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))
        to = request.GET.get('to','')

        data = {
            'error': '',
            'to': to
        }
        return render_to_response(request,self.TEMPLATE,data=data)
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        to = request.GET.get('to','')

        data = {}
        exists = User.objects.filter(username=username).exists()
        data['error'] = '不存在该用户'
        if not exists:
            return render_to_response(request,self.TEMPLATE,data=data)

        user = authenticate(username=username,password=password)
        if not user:
            data['error'] = '密码错误'
            return render_to_response(request,self.TEMPLATE,data=data)

        if not user.is_superuser:
            data['error'] = '你权限被噶，无法登录，请联系其他管理员处理'
            return render_to_response(request,self.TEMPLATE,data=data)
        # 登录
        login(request,user)
        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('login'))
class Admin(View):
    TEMPLATE = '/dashboard/admin/admin.html'
    @dashboard_auth
    def get(self,request):
        users = User.objects.all()
        page = request.GET.get('page',1)
        p = Paginator(users,4)
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(page).object_list
        total_page = p.num_pages
        data = {
            'users': current_page,
            'total': total_page,
            'current_page': int(page)
        }
        # print(users)
        return render_to_response(request,self.TEMPLATE,data=data)

class UpdateAdminStatus(View):
    def get(self,request):
        status = request.GET.get('status', 'on')
        _status = True if status == 'on' else False
        request.user.is_superuser = _status
        # print('current_user',request.user)
        # request.user.save()
        user_id = request.GET.get('user_id')
        user = User.objects.filter(id = user_id).exclude(id = request.user.id)
        user.update(is_superuser = _status)
        #打印当前修改的用户的user_id
        print('用户的user_id:', request.user.id)
        return redirect(reverse('dashboard_admin'))