from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self,data):
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("username is taken")
        return data

    def create(self,validated_data):
        print("Hello World")
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    def validate(self,data):
        if not User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("account not found")
        return data

    def get_jwt_token(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if not user:
            return{'message':'invalid credentials','data':{}}
        
        refresh=RefreshToken.for_user(user)
        return{'message':'login success','data':{'token':{'refresh': str(refresh),
        'access': str(refresh.access_token)}}}
