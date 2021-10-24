from django.db import models
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User1(AbstractUser):
    ROLE_CHOICES = (
        ("Author", "Author"),
        ("Student", "Student"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user_roles = models.CharField(choices=ROLE_CHOICES, default="Student", max_length=50)
    contact = models.IntegerField(max_length=10, null=True)
    Address = models.TextField(blank=True)
    city = models.CharField(max_length=50)
    education = models.CharField(max_length=250)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now())
    updated_date = models.DateTimeField(default=now())

    def __str__(self):
        return self.email

