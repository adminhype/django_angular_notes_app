from .serializers import NoteSerializer
from notes_app.models import Note
from rest_framework import viewsets


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
