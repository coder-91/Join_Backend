from rest_framework import serializers

from subtask.serializers import SubtaskSerializer
from task.models import Task
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Serializes a task object"""
    subtasks = SubtaskSerializer(many=True)
    users = UserSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_to', 'created', 'updated', 'priority', 'category', 'status',
                  'subtasks', 'users']
        read_only_fields = ['created', 'updated', 'users']
