from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer, UserInfoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, UserInfo


def home(request):
    return HttpResponse("Health Check!")


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # (id: 1)
    def get_queryset(self):
        user = self.request.user
        return Note.objects.all()

    # (id: 1)
    # queryset = Note.objects.all()

    # (id: 1) - Original
    # def get_queryset(self):
    #     user = self.request.user
    #     return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # (id: 3)
    # def get_queryset(self):
    #     user = self.request.user
    #     return Note.objects.filter(author=user)
    # (id: 3)
    def get_queryset(self):
        user = self.request.user
        return Note.objects.all()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserInfoListCreate(generics.ListCreateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    # (id: 1)
    def get_queryset(self):
        user = self.request.user
        return UserInfo.objects.all()

    # (id: 1)
    # queryset = UserInfo.objects.all()

    # (id: 1) - Original
    # def get_queryset(self):
    #     user = self.request.user
    #     return UserInfo.objects.filter(author=user)

    #  (id: 2)
    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save(author=self.request.user)
    #     else:
    #         print(serializer.errors)

    # (id: 4)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)



class UserInfoDelete(generics.DestroyAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    # (id: 3)
    # def get_queryset(self):
    #     user = self.request.user
    #     return Note.objects.filter(author=user)
    # (id: 3)
    def get_queryset(self):
        user = self.request.user
        return UserInfo.objects.all()