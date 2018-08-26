from django.conf.urls import url
from django.contrib import admin

from user.views import show_login_views, do_login_views, show_register_views, do_register_views, do_answer_views

urlpatterns = [
    # 用户请求登录页面
    url(r'^login/$', show_login_views),
    # 处理用户从登录页面请求的信息
    url(r'^dologin/$', do_login_views),
    # 用户请求注册页面
    url(r'^register/$', show_register_views),
    # 处理用户注册请求
    url(r'^doregister/$', do_register_views),
    # 用户登录之后进入功能选择
    # url(r'^dochoice/$', do_choice_views),
    # 进入答题系统
    url(r'^answer/$', do_answer_views),
]