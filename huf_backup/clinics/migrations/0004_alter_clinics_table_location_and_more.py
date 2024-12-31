# Generated by Django 4.2.7 on 2024-12-30 18:32

import clinics.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinics", "0003_clinics_table_address_clinics_table_locationlink_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinics_table",
            name="location",
            field=models.CharField(
                max_length=2000, validators=[clinics.models.validate_small_letters]
            ),
        ),
        migrations.AlterField(
            model_name="historicalclinics_table",
            name="location",
            field=models.CharField(
                max_length=2000, validators=[clinics.models.validate_small_letters]
            ),
        ),
    ]
