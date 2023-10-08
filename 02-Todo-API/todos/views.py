from rest_framework import generics
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

from distutils.util import strtobool


class TodoList(generics.ListCreateAPIView):
    """
    List view for todos
    Allows only GET and POST HTTP methods.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # Overriding list method of view class
    def list(self, request):
        queryset = self.get_queryset()

        # Getting URL parameters using 'self.request.get_query_params'
        completed_param = request.query_params.get("completed")
        sort_by = request.query_params.get("sort_by")

        # Converting completed_param value to a Boolean value (with a try-except block)
        if completed_param is not None:
            try:
                completed = bool(strtobool(completed_param.lower()))
            except (ValueError, AttributeError):
                completed = None
        else:
            completed = None

        # Applying filters based on URL parameters
        if completed is not None:
            queryset = queryset.filter(completed=completed)

        if sort_by == "date_updated":
            queryset = queryset.order_by("date_updated")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TodoDetail(generics.RetrieveUpdateAPIView):
    """
    Detail view for todo object.
    Allows only GET and PATCH HTTP methods
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
