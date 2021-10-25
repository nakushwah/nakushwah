from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the fields of book for doing CRUD operations
    """

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validate_data):
        """creating books object """
        return Book.objects.create(**validate_data)
