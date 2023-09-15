from rest_framework import routers

from books.viewset import BooksViewSet


lms_route = routers.DefaultRouter()

lms_route.register('books', BooksViewSet)
