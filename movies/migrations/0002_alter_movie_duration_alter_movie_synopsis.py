# Generated by Django 4.1.6 on 2023-02-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(blank=True, null=True),
        ),
    ]