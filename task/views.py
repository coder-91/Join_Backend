from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from task.models import Task
from task.serializers import TaskSerializer
from utils.utils import handle_serialization


class TaskView(APIView):
    def get(self, request):
        """Returns a list of tasks"""
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        return handle_serialization(serializer, status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get_task(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk=None):
        task = self.get_task(pk)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        task = self.get_task(pk)
        serializer = TaskSerializer(task, data=request.data)
        return handle_serialization(serializer, status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        task = self.get_task(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        return handle_serialization(serializer, status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        task = self.get_task(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
