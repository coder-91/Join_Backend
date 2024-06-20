from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializes a task object"""

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'dueTo', 'created', 'updated', 'priority', 'category', 'status',
                  'subtasks', 'users']
