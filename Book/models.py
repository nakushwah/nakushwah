""" creating model for storing book's data ,
    used uuid for creating unique id for each object of book table ,
    and for creating author and student choices used user1 model filter by user_roles
"""

import uuid
from django.db import models
from UserAuth.models import User1


class Book(models.Model):
    """ model for Books """
    Author_choice = sorted([(item.email, item.email) for item in
                            User1.objects.filter(user_roles="Author")])
    Student_choice = sorted([(item.email, item.email) for item in
                             User1.objects.filter(user_roles="Student")])

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                          editable=False)
    title = models.CharField(max_length=250)
    author = models.CharField(choices=Author_choice,max_length=50,
                              null=True)
    issue_to_user = models.CharField(choices=Student_choice,
                                     max_length=50, null=True)
    issue_from = models.DateTimeField(null=True)
    issue_to = models.DateTimeField(null=True)
    published_date = models.DateTimeField()
    price = models.FloatField(default=00.00)
    penalty = models.IntegerField(default=00)

    def __str__(self):
        return self.title


