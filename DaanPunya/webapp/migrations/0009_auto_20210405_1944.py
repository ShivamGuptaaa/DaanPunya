# Generated by Django 3.0.8 on 2021-04-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20210327_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='update',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
