# Generated by Django 3.0.1 on 2020-02-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200209_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio-images'),
        ),
    ]
