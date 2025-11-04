from django.db import models


class Note(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    marked = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
