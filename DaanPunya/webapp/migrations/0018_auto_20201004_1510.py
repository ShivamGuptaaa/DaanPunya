# Generated by Django 3.0.8 on 2020-10-04 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20201004_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]