# Generated by Django 5.2.4 on 2025-07-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="currency",
            field=models.CharField(default="USD", max_length=3),
        ),
    ]
