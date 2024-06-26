from django.db import models
from django.utils import timezone

from user.models import User


# Create your models here.
class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        URGENT = "URGENT"

    class Category(models.TextChoices):
        TECHNICAL_TASK = "TECHNICAL_TASK"
        USER_STORY = "USER_STORY"

    class TaskStatus(models.TextChoices):
        TO_DO = "TO_DO"
        AWAIT_FEEDBACK = "AWAIT_FEEDBACK"
        IN_PROGRESS = "IN_PROGRESS"
        DONE = "DONE"

    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True)
    due_to = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)
    priority = models.TextField(choices=Priority.choices)
    category = models.TextField(choices=Category.choices)
    status = models.TextField(choices=TaskStatus.choices)
    users = models.ManyToManyField(User, blank=True, related_name='tasks')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

