# Generated by Django 3.0.8 on 2020-10-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20201003_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='qauntity',
            field=models.IntegerField(default=0),
        ),
    ]
