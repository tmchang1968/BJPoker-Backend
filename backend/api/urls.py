from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("user-info/", views.UserInfoListCreate.as_view(), name="user-info-list"),
    path("user-info/delete/<int:pk>/", views.UserInfoDelete.as_view(), name="delete-user-info"),
]
