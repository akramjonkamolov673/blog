# Generated by Django 4.2.6 on 2023-10-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_postmodel_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='countlike',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='is_liked',
        ),
    ]
