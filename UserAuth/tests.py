import json
from rest_framework import status
from django.urls import reverse
from .models import User1
from .serializers import UserSerializer
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

# initialize the APIClient app
client = APIClient()



class TestLogIn(TestCase):

    def setUp(self):
        self.crete_user = User1.objects.create_user(
            username="kumar",
            first_name="kumar",
            last_name="last_name",
            email="email@gmail.com",
            password="one234"
        )
        self.first_payload = {
            "username": "kumar",
            "password": "one234"
        }
        self.second_payload = {
            "username": "admin12",
            "password": "1234"
        }

    def test_login(self):
        """Test module for valid payload """

        response = client.post(
            reverse('LogIn'),
            data=json.dumps(self.first_payload),
            content_type="Application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid(self):
        """Test module for Invalid payload """
        response = client.post(
            reverse('LogIn'),
            data=json.dumps(self.second_payload),
            content_type="Application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestGetUser1(APITestCase):
    """ Test class for User1 Model"""

    def setUp(self):
        """ module for defining values for next test """
        self.crete_user = User1.objects.create_user(
            username="kumar",
            first_name="kumar",
            last_name="last_name",
            email="email@gmail.com",
            password="one234"
        )
        self.first_payload = {
            "username": "kumar",
            "password": "one234"

        }
        self.user = client.post(
            reverse('LogIn'),
            data=json.dumps(self.first_payload),
            content_type="Application/json")


    def test_get_User1s(self):
        """
            Test module to getting all User  API
        """
        response = client.get(
            reverse('ListCreateUser'))
        User1s = User1.objects.all()
        serializer = UserSerializer(User1s, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPostUser(TestCase):
    """
    A test class for creating User by valid aor invalid payload
    """

    def setUp(self):
        self.invalid_payload = {
            "username": "kumar1234",
            "first_name": "nk",
            "last_name": "a",
            "email": "kumar1243@gmail.c",
            "user_roles": "Author",
            "contact": 123456789,
            "Address": "ds",
            "city": "kghjh",
            "education": "dsdfds",
            "password": "one234"
        }

        self.valid_payload = {
            "username": "NDK12347",
            "first_name": "kumar21",
            "last_name": "ndk22",
            "email": "kumar124357@gmail.com",
            "user_roles": "Author",
            "contact": 2134567890,
            "Address": "dfdfs",
            "city": "sdfdsf",
            "education": "fsdf",
            "password": "one23four",
            "created_date": "2021-10-22T13:43:05.257864Z",
            "updated_date": "2021-10-22T13:43:05.257878Z",
        }

    def test_valid_post_User(self):
        """
         Test module for creating  single user with valid payload
        """
        response = client.post(
            reverse('ListCreateUser'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_post_User1(self):
        """
         Test module for creating  single with invalid payload
        """
        response = client.post(
            reverse('ListCreateUser'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateUser(TestCase):
    """Test class for updating User1 """

    def setUp(self):
        self.obj1 = User1.objects.create(
            username="NDK1234",
            first_name="kumar21",
            last_name="ndk22",
            email="kumar12443@gmail.com",
            date_joined="2021-10-22T21:13:00Z",
            user_roles="Author",
            contact=2134567890,
            Address="dfdfs",
            city="sdfdsf",
            education="fsdf",
            is_verified=True,
            created_date="2021-10-22T13:43:05.257864Z",
            updated_date="2021-10-22T13:43:05.257878Z",

        )

        self.invalid_payload = {
            "username": "kumar1234",
            "first_name": "nk",
            "last_name": "a",
            "email": "kumar1243@gmail.",
            "user_roles": "Author",
            "contact": "123456789",
            "Address": "ds",
            "city": "kghjh",
            "education": "dsdfds",
            "is_verified": True,
            "password": "one23four",
            "created_date": "2021-10-22T08:00:48Z",
            "updated_date": "2021-10-22T08:00:48Z"
        }

        self.valid_payload = {
            "username": "NDK12347",
            "first_name": "kumar21",
            "last_name": "ndk22",
            "email": "kumar124357@gmail.com",
            "user_roles": "Author",
            "contact": 2134567890,
            "Address": "dfdfs",
            "city": "sdfdsf",
            "education": "fsdf",
            "password": "one23four",
            "created_date": "2021-10-22T13:43:05.257864Z",
            "updated_date": "2021-10-22T13:43:05.257878Z",
        }

    def test_update_User(self):
        """ Test module for update valid payload and User by id"""

        response = client.put(
            reverse('UpdateUser', kwargs={'pk': self.obj1.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_User_with_invalid_payload(self):
        """ Test module for update with Invalid payload User1 by id """
        response = client.put(
            reverse('UpdateUser', kwargs={'pk': self.obj1.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#
class TestUser1Delete(TestCase):
    def setUp(self):
        self.obj1 = User1.objects.create(
            username="NDK1234",
            first_name="kumar21",
            last_name="ndk22",
            email="kumar12443@gmail.com",
            date_joined="2021-10-22T21:13:00Z",
            user_roles="Author",
            contact=2134567890,
            Address="dfdfs",
            city="sdfdsf",
            education="fsdf",
            is_verified=True,
            created_date="2021-10-22T13:43:05.257864Z",
            updated_date="2021-10-22T13:43:05.257878Z",

        )

    def test_valid_delete_User1(self):
        """ deleting the User1 object by valid id """

        response = client.delete(reverse('UpdateUser', kwargs={'pk': self.obj1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_User1(self):
        """ deleting the User1 object by invalid id """

        response = client.delete(reverse('UpdateUser', kwargs={'pk': 12}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestRegister(TestCase):

    def setUp(self):
        self.valid = {
            "username": "narendra09",
            "first_name": "Nk",
            "email": "hdkkjd@gmail.com",
            "last_name": "kushwah",
            "password": "onw23for",
            "password2": "onw23for",
        }

        self.invalid = {
            "username": "kumar1234",
            # "first_name": "nk",
            "last_name": "kushwah",
            "password": "onw23for",
            "password2": "onw23for",
            "email": "kumar1243@gmail.com"
        }

    def test_register_with_valid(self):
        response = client.post(
            reverse('RegisterView'),
            data=json.dumps(self.valid),
            content_type="Application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_invalid(self):
        response = client.post(
            reverse('RegisterView'),
            data=json.dumps(self.invalid),
            content_type="Application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
