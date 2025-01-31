from rest_framework.serializers import ModelSerializer
from notesapp.models import Category
from notesapp.models import Note

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title','body','updated','created','categoryId']
