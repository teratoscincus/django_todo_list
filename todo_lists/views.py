from django.shortcuts import render


def index(request):
    """Displays the index view o the Todo List app."""
    return render(request, "todo_lists/index.html")
