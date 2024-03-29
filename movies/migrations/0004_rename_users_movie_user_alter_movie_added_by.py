# Generated by Django 4.1.6 on 2023-02-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_movieorder_movie_users"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="users",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="movie",
            name="added_by",
            field=models.EmailField(max_length=254),
        ),
    ]
