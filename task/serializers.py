from rest_framework import serializers

from subtask.serializers import SubtaskSerializer
from task.models import Task
from user.models import User
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Serializes a task object"""
    subtasks = SubtaskSerializer(many=True, required=False)
    users = UserSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_to', 'created', 'updated', 'priority', 'category', 'status',
                  'subtasks', 'users']
        read_only_fields = ['created', 'updated']

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        task = Task.objects.create(**validated_data)

        if users_data is not None:
            for user_data in users_data:
                user = User.objects.get(id=user_data['id'])
                task.users.add(user)

        return task
