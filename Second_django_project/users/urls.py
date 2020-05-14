# 必须定义一个路由样式列表：路由样式列表名字必须叫urlpatterns
from django.urls import path
from . import views

# 子路由样式表
urlpatterns = [
    # 使用路由匹配请求地址，没匹配成功一个就执行对应的函数视图逻辑
    # path('网络地址正则表达式', 视图函数名)
    # 用户注册：http://127.0.0.1:8000/users/register/
    path('users/register/', views.register)
]