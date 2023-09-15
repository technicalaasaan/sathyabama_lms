"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path
from books.urls import lms_route
from books.views import GetBook, UpdateBook, home, contact, create_view, CreateBook, get_books, update_books
# from

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('books/', create_view, name='books'),
    path('books/get/', get_books),
    path('books/update/', update_books),
    path('books/<pk>/update/', UpdateBook.as_view()),
    path('books_cls/', CreateBook.as_view()),
    path('books_cls/get/', GetBook.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += [
    path('api/', include(lms_route.urls)),
]
