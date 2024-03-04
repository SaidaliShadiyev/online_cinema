# Generated by Django 5.0.2 on 2024-03-02 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('year', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('premier', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.genre')),
            ],
        ),
    ]
