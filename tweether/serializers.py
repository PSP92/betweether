from tweether.models import User, Tweets
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import Group, User


class UserSerializer(ModelSerializer):
     class Meta:
         model = User
         fields = ["id", "name", "email"]

class TweetsSerializer(ModelSerializer):
    class Meta:
        model = Tweets
        fields = ["id", "body", "img", "likes", "tags"]

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
