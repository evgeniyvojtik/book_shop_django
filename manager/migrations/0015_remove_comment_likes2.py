# Generated by Django 3.1.4 on 2020-12-07 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20201207_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes2',
        ),
    ]
