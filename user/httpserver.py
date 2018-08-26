from django.http import HttpResponse


def handler(user_list,email,request):
    while True:
        if len(user_list) < 3:
            return HttpResponse('在线人数为 ' + str(len(user_list)) + '人，人数3人才能开始答题')
        else:
            return HttpResponse('在线人数为 ' + str(len(user_list)) + '人，开始答题')
