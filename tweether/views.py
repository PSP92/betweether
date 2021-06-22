from django.shortcuts import render
from tweether.models import Logger, Tweets
from django.contrib.auth.models import User, Group
from tweether.serializers import LoggerSerializer, TweetsSerializer, UserSerializer, GroupSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny # IsAuthenticated
# from rest_framework_simplejwt import authentication
# Create your views here.


class LoggerViews(ModelViewSet):
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer
    permission_classes = [AllowAny]
    #  permission_classes = [IsAuthenticated]
    # authentication_classes = (authentication.JWTAuthentication,)

class TweetsViews(ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer
    permission_classes = [AllowAny]
    #  permission_classes = [IsAuthenticated]
    # authentication_classes = (authentication.JWTAuthentication,)


class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    


class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]
    #  permission_classes = [IsAuthenticated]
    # authentication_classes = (authentication.JWTAuthentication,)
