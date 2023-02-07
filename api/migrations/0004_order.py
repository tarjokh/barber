# Generated by Django 3.0 on 2023-02-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('count_of_people', models.FloatField(null=True)),
                ('comment', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]