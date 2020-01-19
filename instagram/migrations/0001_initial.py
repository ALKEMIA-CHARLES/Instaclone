# Generated by Django 3.0.2 on 2020-01-19 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBUSER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('db_comment', models.CharField(max_length=100)),
                ('likes', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='loggedinUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.TextField(blank=True)),
                ('Bio', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100)),
                ('loggedin_user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.loggedinUser')),
            ],
        ),
    ]
