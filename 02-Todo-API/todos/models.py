from django.db import models


class Todo(models.Model):
    """
    Model for Todo
    """

    todo = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo
