# Generated by Django 3.0.1 on 2020-02-09 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200209_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='protfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio'),
        ),
    ]