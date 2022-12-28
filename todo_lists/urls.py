"""URL patterns for the Todo List app."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
