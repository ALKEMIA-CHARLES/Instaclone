# Generated by Django 3.0.2 on 2020-01-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0012_post_figure'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbuser',
            name='caption',
            field=models.TextField(max_length=500, null=True),
        ),
    ]