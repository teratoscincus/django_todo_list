from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=200, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.heading}"


class Note(models.Model):
    """Additional notes for the Entry model."""

    parent_entry = models.ForeignKey(Entry, on_delete=models.PROTECT)
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=200, blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.heading}"
