# Generated by Django 3.0.8 on 2020-10-03 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_medicine_expiry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='pub_date',
        ),
    ]
