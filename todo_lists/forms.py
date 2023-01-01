from django.forms import ModelForm

from todo_lists import models


class EntryForm(ModelForm):
    class Meta:
        model = models.Entry
        fields = [
            "heading",
            "text",
        ]


class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = [
            "heading",
            "text",
        ]
