# Generated by Django 3.0.8 on 2020-11-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0033_auto_20201120_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org_update',
            name='mode_del',
            field=models.CharField(choices=[('courier', 'courier'), ('org_pick', 'pickup by org')], max_length=50),
        ),
    ]