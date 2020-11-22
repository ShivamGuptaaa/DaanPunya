# Generated by Django 3.0.8 on 2020-11-17 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0027_auto_20201115_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='user_email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
