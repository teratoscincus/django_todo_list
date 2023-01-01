from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from . import models
from . import forms


def is_user_entry_owner(request, entry):
    """
    Checks if the current user is the owner of an entry.

    The entry parameter expects an instance of the Entry model.

    Returns a boolean value.
    """
    if entry.owner == request.user:
        return True
    else:
        return False


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


def new_entry(request):
    if request.method == "POST":
        # Populate form with data from request
        form = forms.EntryForm(request.POST)

        # Validate form and redirect user.
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()

            return redirect("todo_lists:index")
    else:
        # Create blank form.
        form = forms.EntryForm()

    # Display blank or invalid form.
    context = {
        "form": form,
    }
    return render(request, "todo_lists/new_entry.html", context)


def new_note(request, parent_entry_id):
    # Init parent Entry instance.
    entry = get_object_or_404(models.Entry, id=parent_entry_id)

    # Prevent non owner users from making notes to entry.
    if not is_user_entry_owner(request, entry):
        raise Http404

    if request.method == "POST":
        # Populate form with data from request
        form = forms.NoteForm(request.POST)

        # Validate form and redirect user.
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.parent_entry = entry
            new_note.save()

            return redirect("todo_lists:index")
    else:
        # Create blank form.
        form = forms.NoteForm()

    # Display blank or invalid form.
    context = {
        "form": form,
        "entry": entry,
    }
    return render(request, "todo_lists/new_note.html", context)
