# Generated by Django 3.0.8 on 2020-10-03 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_remove_medicine_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='qauntity',
        ),
    ]
