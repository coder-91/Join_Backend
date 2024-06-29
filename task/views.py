from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task.models import Task
from task.serializers import ReadTaskSerializer, WriteTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReadTaskSerializer
        return WriteTaskSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = WriteTaskSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        task = write_serializer.save()

        read_serializer = ReadTaskSerializer(task)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)
