# Generated by Django 5.0.1 on 2024-01-31 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0012_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
    ]
