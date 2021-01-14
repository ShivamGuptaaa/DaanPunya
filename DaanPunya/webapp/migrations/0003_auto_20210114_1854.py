# Generated by Django 3.0.8 on 2021-01-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210114_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnr_update',
            name='mode_del',
            field=models.CharField(choices=[('Not Selected', None), ('org_pick', 'pickup by org'), ('courier', 'courier')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='cert_num',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='phNum',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='reg_num',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='org_update',
            name='mode_del',
            field=models.CharField(choices=[('Not Selected', None), ('org_pick', 'pickup by org'), ('courier', 'courier')], max_length=50),
        ),
    ]
