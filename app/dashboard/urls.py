# coding:utf-8
from django.urls import path
from app.dashboard.views.base import Index
from app.dashboard.views.auth import Login,Logout,Admin,UpdateAdminStatus
from app.dashboard.views.video import OtherVideo,VideoSubUrl,VideoSubStar,StarDelete

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
    path('admin/update/status',UpdateAdminStatus.as_view(),name='admin_update_status'),
    #视频页
    path('video/other',OtherVideo.as_view(),name='other_video'),
    #附属信息跳转页
    path('video/videosub/<int:video_id>',VideoSubUrl.as_view(),name='video_sub'),
    #附属-演员信息提交接口
    path('video/videosub/videostar',VideoSubStar.as_view(),name='video_sub_star'),
    #附属-演员信息删除接口
    path('video/videosub/videostar/delete/<int:star_id>/<int:video_id>',StarDelete.as_view(),name='star_delete')


]