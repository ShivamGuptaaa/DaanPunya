# Generated by Django 3.0.8 on 2020-10-03 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20201003_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='expiry_date',
        ),
    ]
