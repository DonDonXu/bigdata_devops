from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
        error_msg = ""
        if request.method == "POST":
        # 获取用户通过POST提交过来的数据
                user = request.POST.get('user',None)
                pwd = request.POST.get('pwd',None)
                if user == 'zfno11' and pwd == "N$nIpms1":
#如果验证通过 就跳转到功能页面，并且设置cookie
                        response=render_to_response('function.html')
                        response.set_cookie('username',user,40)
                        return response
                ##设置cookie
                else:
            # 用户密码不配
                        error_msg = "用户名或密码错误"
                return render(request,'login.html', {'error_msg': error_msg})
        else:
                return render(request,'login.html')



# Create your views here.
