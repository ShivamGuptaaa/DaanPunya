# Generated by Django 3.0.8 on 2020-11-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0044_auto_20201121_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org_update',
            name='mode_del',
            field=models.CharField(choices=[('org_pick', 'pickup by org'), ('courier', 'courier')], max_length=50),
        ),
    ]
