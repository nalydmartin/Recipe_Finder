# Generated by Django 2.2 on 2020-11-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_recipe_cooktime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='comments',
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
