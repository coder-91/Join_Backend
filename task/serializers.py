from rest_framework import serializers

from subtask.serializers import SubtaskSerializer
from task.models import Task
from user.models import User
from user.serializers import UserSerializer


class BaseTaskSerializer(serializers.ModelSerializer):
    """Serializes a task object"""
    subtasks = SubtaskSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_to', 'created', 'updated', 'priority', 'category', 'status',
                  'subtasks', 'users']
        read_only_fields = ['created', 'updated']

    def create(self, validated_data):
        users_data = validated_data.pop('users', [])
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)

        for user_data in users_data:
            user = User.objects.get(email=user_data)
            task.users.add(user)

        for subtask_data in subtasks_data:
            subtask_data['task_id'] = task.id
            SubtaskSerializer().create(validated_data=subtask_data)

        return task


class WriteTaskSerializer(BaseTaskSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)


class ReadTaskSerializer(BaseTaskSerializer):
    users = UserSerializer(many=True, required=False)