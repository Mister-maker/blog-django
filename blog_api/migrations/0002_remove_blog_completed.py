# Generated by Django 5.0.7 on 2024-07-22 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='completed',
        ),
    ]
