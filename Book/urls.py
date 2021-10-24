from django.urls import path
from .views import PostBooks, UpdateBooks

urlpatterns = [
    path("get_books/", PostBooks.as_view(), name="get_create_books"),
    path("edit_books/<pk>/", UpdateBooks.as_view(), name="edit_books"),

]
