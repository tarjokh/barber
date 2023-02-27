# Generated by Django 3.0 on 2023-02-27 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230223_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150, null=True)),
                ('stars', models.IntegerField(null=True)),
                ('time', models.TimeField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.AddField(
            model_name='restaurants',
            name='rate',
            field=models.ManyToManyField(to='api.Rates'),
        ),
    ]