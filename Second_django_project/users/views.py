from django.shortcuts import render
# 导入构造响应对象的模块（http模块：时Django封装的处理网络的模块）
from django import http

# Create your views here.


# 实现函数视图的代码


def register(request):
    """用户注册函数视图，也是函数，需要调用执行"""
    # http://127.0.0.1:8000/users/register/
    # :param request：请求对象，是由Django封装好的，并且传递至此
    # :return 响应对象
    # 用户注册要实现的相关逻辑
    return http.HttpResponse("这是第一个用户注册页面")


# def register("请求对象")
#     用户注册函数视图
#     return 响应对象