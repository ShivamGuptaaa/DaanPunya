# Generated by Django 3.0.8 on 2020-10-04 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20201004_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='pincode',
            new_name='zipcode',
        ),
    ]
