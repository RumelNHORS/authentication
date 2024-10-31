from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework import generics
from mainapp.models import Book
from .serializers import BookSerializer

class ListBooksAPI(generics.ListAPIView):
    authentication_classes=[ SessionAuthentication ]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
