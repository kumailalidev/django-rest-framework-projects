from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for todo
    """

    class Meta:
        model = Todo
        fields = "__all__"
