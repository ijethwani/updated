# Generated by Django 3.0 on 2020-01-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20200128_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about_you',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='author',
            name='profession',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]