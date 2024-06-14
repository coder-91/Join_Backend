from rest_framework import serializers
from contact.serializers import ContactSerializer
from subtask.serializers import SubtaskSerializer
from task.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    contacts = ContactSerializer(many=True)
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'dueTo', 'created', 'updated', 'priority', 'category', 'status',
                  'subtasks', 'contacts']
