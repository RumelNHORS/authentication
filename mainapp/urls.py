from django.urls import path
from .views import ListBooksAPI


urlpatterns = [
    path('api/books/', ListBooksAPI.as_view(), name='list-books'),
]