# Generated by Django 4.1.7 on 2023-04-04 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footer", "0002_alter_footer_table_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 12, 16, 42, 60941)
            ),
        ),
    ]
