from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("user-info/", views.UserInfoListCreate.as_view(), name="user-info-list"),
    path("user-info/delete/<int:pk>/", views.UserInfoDelete.as_view(), name="delete-user-info"),
]
