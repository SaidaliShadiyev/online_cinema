# Generated by Django 5.0.2 on 2024-03-03 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_rename_name_genre_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='country',
        ),
        migrations.RemoveField(
            model_name='film',
            name='premier',
        ),
    ]