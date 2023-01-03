"""URL patterns for the Todo List app."""

from django.urls import path

from . import views

app_name = "todo_lists"
urlpatterns = [
    path("", views.index, name="index"),
    path("new_entry/", views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    path("new_note/<int:parent_entry_id>/", views.new_note, name="new_note"),
    path(
        "edit_note/<int:note_id>/<int:parent_entry_id>/",
        views.edit_note,
        name="edit_note",
    ),
]
