# Generated by Django 5.0.4 on 2024-04-05 07:23

import phone_field.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("all_api", "0003_customuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=phone_field.models.PhoneField(
                blank=True, help_text="Telefon Numarasını Giriniz", max_length=31
            ),
        ),
    ]
