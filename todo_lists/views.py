from django.shortcuts import render

from . import models


def index(request):
    """Displays the index view o the Todo List app."""
    # Get entries belonging to current user.
    entries = models.Entry.objects.filter(owner=request.user.id)

    # Get all notes referencing an entry in entries as a flat list.
    notes = []
    for entry in entries:
        query_set = models.Note.objects.filter(parent_entry__id=entry.id)
        for obj in query_set:
            notes.append(obj)

    context = {
        "entries": entries,
        "notes": notes,
    }
    return render(request, "todo_lists/index.html", context)
