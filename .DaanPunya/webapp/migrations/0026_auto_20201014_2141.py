# Generated by Django 3.0.8 on 2020-10-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_auto_20201014_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='MedPresc',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
