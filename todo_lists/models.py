from django.db import models


class TodoListEntry(models.Model):
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
