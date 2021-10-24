# Generated by Django 3.2.8 on 2021-10-22 08:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c5f4e188-dccc-4701-829d-a310cffc1b79'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='issue_to_user',
            field=models.CharField(choices=[('admin@gmail.com', 'admin@gmail.com'), ('kumar123@gmail.com', 'kumar123@gmail.com'), ('kumar1243@gmail.com', 'kumar1243@gmail.com'), ('kumar@gmail.com', 'kumar@gmail.com'), ('narendrakush@gmail.com', 'narendrakush@gmail.com')], max_length=50, null=True),
        ),
    ]
