# Generated by Django 3.0.8 on 2020-10-03 12:13

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_remove_medicine_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicine',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='medicine',
            name='qauntity',
            field=models.IntegerField(default=0),
        ),
    ]
