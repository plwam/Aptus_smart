# Generated by Django 5.0.4 on 2024-11-13 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date_registered',
        ),
    ]
