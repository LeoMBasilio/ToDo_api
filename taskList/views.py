from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets

class Task_View_Set(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
