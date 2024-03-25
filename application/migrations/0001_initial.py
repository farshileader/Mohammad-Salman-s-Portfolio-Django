# Generated by Django 4.1.3 on 2022-11-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=100, null=True)),
                ("message", models.TextField(max_length=500, null=True)),
            ],
        ),
    ]