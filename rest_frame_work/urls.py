"""rest_frame_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from app01 import views
from app01 import test_views

routers = routers.DefaultRouter()
routers.register("authors", views.AuthorViewSet)
routers.register("books", views.BookViewSet)
routers.register("users", views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # list、create、retrieve等在mixins.py下的类中
    # path('authors/', views.AuthorViewSet.as_view({
    #     'get': 'list',  # 查看所有author
    #     'post': 'create'  # 新增author
    # }), name='author'),
    # path('authors/<int:pk>/', views.AuthorViewSet.as_view({
    #     'get': 'retrieve',  # 查看id为pk的author
    #     'put': 'update',    # 修改id为pk的author
    #     # 'patch': 'partial_update',
    #     'delete': 'destroy',  # 删除
    # }), name='author_detail')
    path('', include(routers.urls)),

    path('login/', views.LoginView.as_view(), name='login'),

    path('test/', test_views.create_t1_t2)
]
