from django.db import models

from task.models import Task


# Create your models here.
class Subtask(models.Model):
    """Subtask object."""
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.description
