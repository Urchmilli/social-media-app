# Generated by Django 5.0.4 on 2024-04-29 15:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="authoe",
            new_name="author",
        ),
    ]
