# Generated by Django 3.0.8 on 2020-11-19 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0030_auto_20201118_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='rq_medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MedName', models.CharField(max_length=30)),
                ('MedQuantity', models.IntegerField()),
                ('MedFor', models.CharField(max_length=10)),
                ('MedReason', models.CharField(max_length=100)),
                ('MedPresc', models.ImageField(upload_to='webapp/images')),
                ('MedDate', models.DateField(default=django.utils.timezone.now)),
                ('user_email', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
