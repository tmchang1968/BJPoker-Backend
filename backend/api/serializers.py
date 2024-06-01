from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["user_no", "user_name", "user_email", "user_birthyear" , "user_birthmonth" , "user_birthday" , "user_azurerole" , "user_blackrole" , "user_professionarea" , "user_workforunit" , "user_title" , "user_sociallinkedin" , "user_socialtwitter" , "user_socialfacebook" , "user_note", "user_info_id", "created_at"]
