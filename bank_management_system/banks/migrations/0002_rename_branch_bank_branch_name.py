# Generated by Django 5.1.6 on 2025-02-10 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("banks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bank",
            old_name="branch",
            new_name="branch_name",
        ),
    ]
