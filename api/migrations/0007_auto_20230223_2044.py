# Generated by Django 3.0 on 2023-02-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ManyToManyField(to='api.Image'),
        ),
        migrations.RemoveField(
            model_name='restaurants',
            name='image',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='image',
            field=models.ManyToManyField(to='api.Image'),
        ),
    ]
