# Generated by Django 3.0.2 on 2020-01-28 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0013_dbuser_caption'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]