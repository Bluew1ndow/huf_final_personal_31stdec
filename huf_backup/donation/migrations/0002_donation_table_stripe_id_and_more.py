# Generated by Django 4.1.7 on 2024-12-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("donation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation_table",
            name="stripe_id",
            field=models.CharField(default="####", max_length=1000),
        ),
        migrations.AddField(
            model_name="historicaldonation_table",
            name="stripe_id",
            field=models.CharField(default="####", max_length=1000),
        ),
    ]
