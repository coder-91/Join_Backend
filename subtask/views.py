from rest_framework import viewsets
from subtask.models import Subtask
from subtask.serializers import SubtaskSerializer


# Create your views here.
class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all().order_by('id')
    serializer_class = SubtaskSerializer
    permission_classes = []