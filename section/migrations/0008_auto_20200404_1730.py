# Generated by Django 3.0.3 on 2020-04-04 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0007_auto_20200404_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='version',
            new_name='ver',
        ),
    ]
