from rest_framework import viewsets

from books.serializers import BooksSerializer
from .models import Books


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
