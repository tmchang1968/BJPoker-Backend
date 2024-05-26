from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]
