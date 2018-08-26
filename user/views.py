from threading import Thread

from django.http import HttpResponse
from django.shortcuts import render

from user.httpserver import handler
from .models import *

# Create your views here.

# 登录的用户请求信息
user_list = list()

# 登录的用户名
uname_set = set()


# 处理用户访问登录页面
# /user/login
def show_login_views(request):
    return render(request, 'login.html')


# 处理用户从页面发过来的请求
# /user/dologin
def do_login_views(request):
    # 如果用户直接通过浏览器访问/user/login
    # 代表用户并没有在登录页面输入用户信息
    # 将页面跳转到登录页面
    if request.POST.get('email') is None:
        return render(request, 'login.html')

    # 接收到用户输入的用户名密码
    email = request.POST.get('email')
    upwd = request.POST.get('upwd')
    print((email,upwd))

    # 从数据库中查找用户输入的信息
    user = User.objects.get(email=email, upwd=upwd) or ''
    print(user)
    # 如果用户输入的用户名存在
    if user:
        # # 数据库中存储的密码
        # user_pwd = user.upwd
        # if upwd == user_pwd:

        # 设置用户登录状态 1：登录 0：游客
        login_flag = 1
        msg = '登录成功'
        #return HttpResponse(msg)
        return render(request, 'choice.html', locals())

    # 用户密码和数据库记录的密码不一致
    # 用户输入的用户名没有记录在数据库中
    msg = '用户名或密码错误'
    return render(request, 'login.html', locals())


# 处理用户访问注册页面
# /user/register
def show_register_views(request):
    return render(request, 'register.html')


# 处理用户注册信息
# /user/doregister
def do_register_views(request):
    # 用户直接输入/user/doregister,则浏览器请求方式为get
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        # 　接受用户的手机号是否存在
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user:
            # 该手机号已经注册,给出提示，回到注册页面
            msg = '邮箱号已经注册'
            return render(request, 'register.html', locals())
        else:
            email = request.POST['email']
            upwd = request.POST['upwd']
            obj = User(email=email, upwd=upwd)
            obj.save()

            login_flag = 1
            msg = '注册成功,自动登录'
            return render(request, 'choice.html', locals())


# 用户请求在线答题
def do_answer_views(request):
    if request.method == 'GET':  # 没有登录直接跳转到登录
        return render(request, 'login.html')

    login_flag = request.POST['login_flag']
    email = request.POST['email']

    # 登录用户信息
    user_list.append(request)
    # 登录的用户名
    uname_set.add(email)

    while True:
        if len(user_list) < 3:
            return HttpResponse('在线人数为 ' + str(len(user_list)) + '人，人数3人才能开始答题')
        else:
            return HttpResponse('在线人数为 ' + str(len(user_list)) + '人，开始答题')
    # return HttpResponse('登录状态' + email + '在线人数' + str(len(user_list)))
