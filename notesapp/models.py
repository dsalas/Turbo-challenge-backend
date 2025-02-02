from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True) 
    body = models.CharField(max_length=500, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    categoryId = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)