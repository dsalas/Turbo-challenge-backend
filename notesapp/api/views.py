from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from notesapp.models import Category
from notesapp.models import Note
from notesapp.api.serializers import CategorySerializer
from notesapp.api.serializers import NoteSerializer

class CategoryApiView(APIView):
    def get(self, request):
        cateogries = Category.objects.all()
        categories_serializer = CategorySerializer(cateogries, many=True)
        return Response(status=status.HTTP_200_OK, data=categories_serializer.data)
    

class NoteApiView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        notes_serializer = NoteSerializer(notes, many=True)
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
