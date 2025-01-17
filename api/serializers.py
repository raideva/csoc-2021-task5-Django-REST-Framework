from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo


"""
TODO:
Create the appropriate Serializer class(es) for implementing
Todo GET (List and Detail), PUT, PATCH and DELETE.
"""


class TodoCreateSerializer(serializers.ModelSerializer):
    """
    TODO:
    Currently, the /todo/create/ endpoint returns only 200 status code,
    after successful Todo creation.

    Modify the below code (if required), so that this endpoint would
    also return the serialized Todo data (id etc.), alongwith 200 status code.
    """
    def save(self, **kwargs):
        data = self.validated_data
        user = self.context['request'].user
        title = data['title']
        todo = Todo.objects.create(creator=user, title=title)
        return {'id': todo.id, 'title': todo.title}
    
    class Meta:
        model = Todo
        fields = ('id', 'title',)


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'creator']

class TodoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']

class CollaboratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'collaborator']
    collaborator = serializers.CharField()


