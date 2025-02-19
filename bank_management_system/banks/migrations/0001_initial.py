# Generated by Django 5.1.6 on 2025-02-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("bank_name", models.CharField(max_length=255, unique=True)),
                ("branch", models.CharField(max_length=255)),
                ("is_islamic", models.BooleanField(default=True)),
            ],
        ),
    ]
