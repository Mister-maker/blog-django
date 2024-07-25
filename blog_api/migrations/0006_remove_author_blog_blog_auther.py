# Generated by Django 5.0.7 on 2024-07-25 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0005_remove_blog_author_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='auther',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='blog_api.author'),
        ),
    ]