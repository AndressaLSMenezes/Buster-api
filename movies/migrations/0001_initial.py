# Generated by Django 4.1.6 on 2023-02-25 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=None, max_length=10)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "G"),
                            ("PG", "Pg"),
                            ("PG-13", "Pg 13"),
                            ("R", "R"),
                            ("NC-17", "Nc 17"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("synopsis", models.TextField(default=None)),
                ("added_by", models.CharField(max_length=127)),
            ],
        ),
    ]
