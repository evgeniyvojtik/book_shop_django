# Generated by Django 3.1.3 on 2020-12-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_book_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
