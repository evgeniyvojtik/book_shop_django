# Generated by Django 3.1.4 on 2020-12-05 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0012_auto_20201205_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.CreateModel(
            name='LikeBookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user_table', to='manager.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user_table', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
        migrations.AddField(
            model_name='book',
            name='likes1',
            field=models.ManyToManyField(related_name='liked_books', through='manager.LikeBookUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
