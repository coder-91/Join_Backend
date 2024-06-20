from rest_framework import viewsets
from task.models import Task
from task.serializers import TaskSerializer


# Developing a DRF RESTAPI for CRUD Operations using ViewSets
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = []
# =================================================


# Developing a DRF RESTAPI for CRUD Operations using Class Based Views
"""
class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        return handle_serialization(serializer, status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST)


class TaskDetailsView(APIView):
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
"""
# =================================================


# Developing a DRF RESTAPI for CRUD Operations using Generic API Views
"""
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
"""
# =================================================


# Developing a DRF RESTAPI for CRUD Operations using Function-Based Views
"""
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def task_details(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
# =================================================

# Developing a DRF RESTAPI for CRUD Operations using Mixins
"""
class TaskList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TaskDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
"""
# =================================================
