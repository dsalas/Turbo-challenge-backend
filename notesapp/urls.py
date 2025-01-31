from django.urls import path
from .api.views import CategoryApiView
from .api.views import NoteApiView
from django.conf import settings

urlpatterns = [
    path('api/categories', CategoryApiView.as_view()),
    path('api/notes', NoteApiView.as_view()),
]