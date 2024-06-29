from rest_framework import serializers
from subtask.models import Subtask
from task.models import Task


class SubtaskSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Subtask
        fields = ['id', 'task_id', 'description', 'is_done']
        read_only_fields = ['id']

    def create(self, validated_data):
        task_id = validated_data.pop('task_id', None)
        task = None
        if task_id:
            task = Task.objects.get(id=task_id)
        subtask = Subtask.objects.create(task=task, **validated_data)
        return subtask
