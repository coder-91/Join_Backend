from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from subtask.models import Subtask
from subtask.serializers import SubtaskSerializer


# Create your views here.
class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all().order_by('id')
    serializer_class = SubtaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

