# Generated by Django 2.2.5 on 2020-02-17 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200205_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
