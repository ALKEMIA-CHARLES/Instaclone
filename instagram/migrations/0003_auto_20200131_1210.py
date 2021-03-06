# Generated by Django 3.0.2 on 2020-01-31 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0002_auto_20200130_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_section',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
