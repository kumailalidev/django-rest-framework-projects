from django.urls import path

from .views import TodoList, TodoDetail

urlpatterns = [
    path("todos/", TodoList.as_view(), name="todos_list"),
    path("todo/<int:pk>/", TodoDetail.as_view(), name="todos_detail"),
]
