from django.contrib import admin

from notesapp.models import Note
from notesapp.models import Category

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','body','updated','created','categoryId']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
