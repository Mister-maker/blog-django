# Generated by Django 5.0.7 on 2024-07-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_remove_blog_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
    ]