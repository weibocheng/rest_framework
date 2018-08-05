from rest_framework import serializers
from . import models


class AuthorModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = "__all__"


class BookModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = "__all__"


class UserModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = "__all__"
