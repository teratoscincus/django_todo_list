from django.db import models


class Entry(models.Model):
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=200)


class Note(models.Model):
    """Additional notes for the Entry model."""

    parent_entry = models.ForeignKey(Entry, on_delete=models.PROTECT)
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
