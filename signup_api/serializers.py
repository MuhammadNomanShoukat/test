from .models import SignUpModel
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.core import exceptions


# ================================================================ SignUpModel Serializer class ======================
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpModel

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'semester',
            'cgpa',
            'uni',
            'phone',
            'address',
        ]

    # this funciton making the password to the django authentication
    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(validated_data['password'])
            user = SignUpModel.objects.create(**validated_data)
            return user



# ============================================================== Login Serializer class for user authentication ========


class LoginSerializer_Data(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    # this function using to authenticate the user along "username" and "password"
    def validate(self, attrs):
        username = attrs.get('username','')
        password = attrs.get('password','')
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    attrs['user']=user
                else:
                    raise exceptions.ValidationError("User not active yet")
            else:
                raise exceptions.ValidationError("User not loggec in")
        else:
            raise exceptions.ValidationError("Given credential not correct")
        return attrs
