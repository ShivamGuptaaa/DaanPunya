# Generated by Django 3.0.8 on 2020-11-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0028_medicine_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='MedPic',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]