# Generated by Django 3.0.2 on 2020-01-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20200122_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggedinuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
