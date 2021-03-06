# Generated by Django 3.0 on 2020-01-25 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200125_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nextt', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previouss', to='posts.Post'),
        ),
    ]
