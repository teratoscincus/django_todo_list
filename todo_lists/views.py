from django.shortcuts import render

from . import models


def index(request):
    """Displays the index view o the Todo List app."""
    entries = models.Entry.objects.all()
    notes = models.Note.objects.all()
    context = {
        "entries": entries,
        "notes": notes,
    }
    return render(request, "todo_lists/index.html", context)
