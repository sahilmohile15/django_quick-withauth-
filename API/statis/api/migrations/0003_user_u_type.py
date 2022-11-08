# Generated by Django 4.1.2 on 2022-11-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename__id_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="u_type",
            field=models.CharField(
                choices=[("parent", "Parent"), ("teacher", "Teacher")],
                default="teacher",
                max_length=255,
            ),
        ),
    ]
