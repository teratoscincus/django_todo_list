"""URL patterns for the Todo List app."""

from django.urls import path

from . import views

app_name = "todo_lists"
urlpatterns = [
    path("", views.index, name="index"),
]
