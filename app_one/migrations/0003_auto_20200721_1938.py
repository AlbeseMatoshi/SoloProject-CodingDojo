# Generated by Django 3.0.6 on 2020-07-21 17:38

import app_one.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_foodtype_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo_path',
            field=models.ImageField(upload_to=app_one.models.images_path),
        ),
    ]
