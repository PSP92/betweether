from django.shortcuts import render
from tweether.models import User, Tweets
from tweether.serializers import UserSerializer, TweetsSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class UserViews(ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer
    #  permission_classes = [permissions.AllowAny]


class TweetsViews(ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer
    # permission_classes = [permissions.AllowAny]
