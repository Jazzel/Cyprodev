# Generated by Django 2.2.5 on 2020-02-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20200216_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='protfolio',
            new_name='portfolio',
        ),
    ]
