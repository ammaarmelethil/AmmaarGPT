# Generated by Django 4.2.9 on 2024-01-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chat",
            name="user",
        ),
        migrations.AlterField(
            model_name="chat",
            name="created_at",
            field=models.DateTimeField(),
        ),
    ]
