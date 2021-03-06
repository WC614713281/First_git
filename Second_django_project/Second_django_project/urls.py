"""Second_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 将子路由包含进总路由
from django.urls import include

# 工程的总路由样式表
urlpatterns = [
    # 默认的后台管理系统的总路由
    path('admin/', admin.site.urls),
    # 将users子应用中的子路由注册给总路由
    # path('', include('子应用.urls'))
    # 每个子应用的子路由只需要注册一次即可
    path('', include('users.urls'))
]
