# Generated by Django 3.0.3 on 2020-03-26 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0004_auto_20200326_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.Xtreme'),
        ),
    ]
