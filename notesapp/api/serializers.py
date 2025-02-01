from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import IntegerField
from rest_framework.serializers import StringRelatedField
from notesapp.models import Category
from notesapp.models import Note

class CategorySerializer(ModelSerializer):
    num_notes = IntegerField()  

    class Meta:
        model = Category
        fields = ['id', 'name','num_notes']

class NoteSerializer(ModelSerializer): 
    class Meta:
        model = Note
        fields = ['id', 'title','body','updated','created','categoryId']

class NoteListSerializer(ModelSerializer):
    categoryName = StringRelatedField(source='name')  
    class Meta:
        model = Note
        fields = ['id', 'title','body','updated','created','categoryId','categoryName']
