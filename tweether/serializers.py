from tweether.models import User, Tweets
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
     class Meta:
         model = User
         fields = ["id", "name", "email"]

class TweetsSerializer(ModelSerializer):
    class Meta:
        model = Tweets
        fields = ["id", "body", "img", "likes", "tags"]
