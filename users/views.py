"""Defines views for the users app."""

from django.shortcuts import render, redirect
from django.contrib.auth import login

from users.forms import RegistrationForm


def register(request):
    if request.method == "POST":
        # Populate form with data from request.
        form = RegistrationForm(request.POST)

        # Validate form and redirect user.
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("todo_lists:index")
    else:
        # Create a blank form.
        form = RegistrationForm()

    # Display blank or invalid form.
    context = {
        "form": form,
    }
    return render(request, "registration/register.html", context)
