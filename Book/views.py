from rest_framework import generics
from rest_framework.permissions import IsAuthenticated ,AllowAny
from .models import Book
from .serializers import BookSerializer


class PostBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)


class UpdateBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

