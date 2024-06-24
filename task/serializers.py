from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializes a task object"""

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_to', 'created', 'updated', 'priority', 'category', 'status',
                  'subtasks', 'users']
        read_only_fields = ['created', 'updated']
