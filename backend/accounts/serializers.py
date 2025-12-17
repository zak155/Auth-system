from djoser.serializers import UserCreateSerializers
from django.contrib.auth import get_user_model
User=get_user_model()

class userCreateSerializer(UserCreateSerializer):
    class meta(UserCreateSerializer.Meta):
        model=User
        fields=('id','email','name','passowrd')