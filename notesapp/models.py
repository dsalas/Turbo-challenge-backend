from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    categoryId = models.IntegerField()

class Category(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)