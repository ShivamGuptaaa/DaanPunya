# Generated by Django 3.0.8 on 2020-10-04 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20201004_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='zipcode',
            new_name='areacode',
        ),
    ]
