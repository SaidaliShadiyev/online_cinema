# Generated by Django 5.0.2 on 2024-03-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_film_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='premier',
            field=models.CharField(max_length=100),
        ),
    ]
