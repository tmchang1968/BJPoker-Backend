from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, UserInfoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, UserInfo


def home(request):
    return HttpResponse("Health Check!")


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserInfoListCreate(generics.ListCreateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserInfo.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)



class UserInfoDelete(generics.DestroyAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserInfo.objects.all()