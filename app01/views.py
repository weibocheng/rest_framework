from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serilizer import *
from app01.utils import *

from app01 import models

"""
class PublishView(View):

    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")


class BookView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    pass


class AuthorView(generics.ListCreateAPIView):
    pass
"""


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = BookModelSerializers


class MyPageNumberPagination(PageNumberPagination):
    # from rest_framework.pagination import PageNumberPagination
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = "size"  # 可以在url上拼接?page=1&size=2设置临时分页显示的条数，
    max_page_size = 2               # max_page_size控制size的最大值


class AuthorViewSet(viewsets.ModelViewSet):
    # from rest_framework import viewsets
    queryset = models.Author.objects.all()
    serializer_class = AuthorModelSerializers
    """ # 针对视图自定制
    pagination_class = MyPageNumberPagination
    pagination_class.page_size = 1
    pagination_class.page_query_param = 'page'
    pagination_class.page_size_query_param = 'size'
    pagination_class.max_page_size = 2
    """


class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuth]

    queryset = models.User.objects.all()
    serializer_class = UserModelSerializers


def get_random_str(user):
    """
    生成一个随机字符串，当作token值
    :param user: 用户名
    :return:
    """
    import hashlib
    import time
    c_time = str(time.time())

    md5 = hashlib.md5(bytes(user, encoding="utf8"))
    md5.update(bytes(c_time, encoding="utf8"))

    return md5.hexdigest()


class LoginView(APIView):
    # from rest_framework.views import APIView
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return HttpResponse("get..")

    def post(self, request):
        name = request.data.get("name")
        pwd = request.data.get("pwd")

        user = models.User.objects.filter(name=name, pwd=pwd).first()
        res = {"state_code": 1000, "msg": None}
        if user:
            # 用户每次登录都更新一个新的token值，并且把token返回给前端
            random_str = get_random_str(user.name)
            models.Token.objects.update_or_create(user=user, defaults={"token": random_str})
            res["token"] = random_str
        else:
            res["state_code"] = 1001  # 错误状态码
            res["msg"] = "用户名或者密码错误"

        import json
        # from rest_framework.response import Response
        return Response(json.dumps(res, ensure_ascii=False))


