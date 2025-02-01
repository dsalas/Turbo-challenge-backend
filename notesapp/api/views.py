from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notesapp.models import Category
from notesapp.models import Note
from notesapp.api.serializers import CategorySerializer
from notesapp.api.serializers import NoteSerializer,NoteListSerializer
from django.db.models import Count
from django.db.models import OuterRef, Subquery
from django.db.models import F

class CategoryApiView(APIView):
    def get(self, request):
        cateogries = Category.objects.annotate(num_notes=Count('note'))
        categories_serializer = CategorySerializer(cateogries, many=True)
        return Response(status=status.HTTP_200_OK, data=categories_serializer.data)
    

class NoteApiView(APIView):
    def get(self, request):
        pk = request.GET.get('id', None)
        if not pk:
            notes = Note.objects.annotate(
                name=Subquery(
                    Category.objects.filter(
                    id=OuterRef('categoryId')
                    ).values('name')
                ))
            notes_serializer = NoteListSerializer(notes, many=True)
            return Response(status=status.HTTP_200_OK, data=notes_serializer.data)
        else:
            note = Note.objects.get(pk=pk)
            notes_serializer = NoteSerializer(note)
            return Response(status=status.HTTP_200_OK, data=notes_serializer.data)
    
    def post(self, request):
        notes_serializer = NoteSerializer(data=request.POST)
        notes_serializer.is_valid(raise_exception=True)
        notes_serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=notes_serializer.data)
    
    def put(self, request):
        pk = request.GET.get('id', None)
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'id is required'})
        note = Note.objects.get(pk=pk)
        notes_serializer = NoteSerializer(note, data=request.POST)
        notes_serializer.is_valid(raise_exception=True)
        notes_serializer.save()
        return Response(status=status.HTTP_200_OK, data=notes_serializer.data)
    

