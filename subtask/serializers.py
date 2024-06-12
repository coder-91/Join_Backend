from rest_framework import serializers
from subtask.models import Subtask


class SubtaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'description', 'is_done', 'task']