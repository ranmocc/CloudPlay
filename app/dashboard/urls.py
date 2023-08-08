# coding:utf-8
from django.urls import path
from app.dashboard.views.base import Index
from app.dashboard.views.auth import Login,Logout,Admin,UpdateAdminStatus

urlpatterns = [
    #首页
    path('',Index.as_view(),name='dashboard_index'),
    #登录
    path('login',Login.as_view(),name='login'),
    #注销
    path('logout',Logout.as_view(),name='logout'),
    #管理员
    path('admin', Admin.as_view(), name='dashboard_admin'),
    #设置管理员
    path('admin/update/status',UpdateAdminStatus.as_view(),name='admin_update_status')
]