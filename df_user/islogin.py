#coding=utf-8
from django.http import HttpResponseRedirect

#如果登录则转到登录页面
def islogin(func):
    def login_fun(request,*args,**kwargs):
        if request.session.get('user_id'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url',request.get_full_path)
            return red
    return login_fun

# http://127.0.0.1:8000/14/?type=10

# request.path:表示当前路径，为/14/
# request.get_full_path:表示为完整路径，为/14/?type=10
# 可以传递参数