import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Book
from .serializers import BookSerializer

client = Client()


class TestGetBook(TestCase):
    """ Test class for Book Model"""

    def setUp(self):
        """ module for defining values for next test """

        self.obj1 = Book.objects.create(
            title="yellowBoy",
            author="admin@gmail.com",
            issue_to_user="narendrakush@gmail.com",
            published_date="2021-10-06T14:58:00Z",
        )

    def test_single_get(self):
        """ Test module for getting single book by id"""

        response = client.get(
            reverse('edit_books', kwargs={'pk': self.obj1.id}))
        books = Book.objects.get(id=self.obj1.id)
        serializer = BookSerializer(books)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_books(self):
        """
            Test module to getting all Books  API
        """
        response = client.get(
            reverse('get_create_books'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPostBook(TestCase):
    """
    A test class for creating books by valid aor invalid payload
    """

    def setUp(self):
        self.invalid_payload = {
            "title": "asd",
            "author": "admin@gmail.com",
            "issue_to_user": "admin@gmail.com",
            "issue_from": "null",
            "issue_to": "null",
            "published_date": "2021-10-06T14:58:00Z",
            "price": 0.0,
            "penalty": 0
        }

        self.valid_payload = {
            "title": "asd123",
            "author": "admin@gmail.com",
            "issue_to_user": "narendrakush@gmail.com",
            "issue_from": "2021-10-06T14:58:00Z",
            "issue_to": "2021-10-06T14:58:00Z",
            "published_date": "2021-10-06T14:58:00Z",
            "price": 0.0,
            "penalty": 0
        }

    def test_valid_post_book(self):
        """
         Test module for creating  single with valid payload
        """
        response = client.post(
            reverse('get_create_books'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_post_book(self):
        """
         Test module for creating  single with invalid payload
        """
        response = client.post(
            reverse('get_create_books'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateBook(TestCase):
    """Test class for updating Book """

    def setUp(self):
        self.obj1 = Book.objects.create(
            title="yellowBoy",
            author="admin@gmail.com",
            issue_to_user="narendrakush@gmail.com",
            published_date="2021-10-06T14:58:00Z",
        )

        self.valid_payload = {
            "title": "yellowBoy",
            "author": "admin@gmail.com",
            "issue_to_user": "narendrakush@gmail.com",
            "issue_from": "2021-10-06T14:58:00Z",
            "issue_to": "2021-10-06T14:58:00Z",
            "published_date": "2021-10-06T14:58:00Z",
            "price": 0.0,
            "penalty": 10
        }

        self.invalid_payload = {
            "title": "yellowBoy",
            "author": "admin123@gmail.com",
            "issue_to_user": "narendrakush@gmail.com",
            "issue_from": "2021-10-06T14:58:00Z",
            "issue_to": "2021-10-06T14:58:00Z",
            "published_date": "2021-10-06T14:58:00Z",
            "price": 0.0,
            "penalty": 10
        }

    def test_update_book(self):
        """ Test module for update valid payload and book by id"""

        response = client.put(
            reverse('edit_books', kwargs={'pk': self.obj1.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_with_invalid_payload(self):
        """ Test module for update with Invalid payload book by id """
        response = client.put(
            reverse('edit_books', kwargs={'pk': self.obj1.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestBookDelete(TestCase):
    def setUp(self):
        self.obj1 = Book.objects.create(
            title="yellowBoy",
            author="admin@gmail.com",
            issue_to_user="narendrakush@gmail.com",
            published_date="2021-10-06T14:58:00Z",
        )

    def test_valid_delete_book(self):
        """ deleting the book object by valid id """

        response = client.delete(reverse('edit_books', kwargs={'pk': self.obj1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_book(self):
        """ deleting the book object by invalid id """

        response = client.delete(reverse('edit_books', kwargs={'pk': 12}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
