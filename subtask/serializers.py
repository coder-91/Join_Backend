from rest_framework import serializers
from subtask.models import Subtask


class SubtaskSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField()

    class Meta:
        model = Subtask
        fields = ['id', 'task_id', 'description', 'is_done']
        read_only_fields = ['id']
