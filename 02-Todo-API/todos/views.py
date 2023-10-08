from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    """
    List view for todos
    Allows only GET and POST HTTP methods.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateAPIView):
    """
    Detail view for todo object.
    Allows only GET and PATCH HTTP methods
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
