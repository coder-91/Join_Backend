from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'dueTo', 'created', 'updated', 'priority', 'category', 'status', 'contacts']