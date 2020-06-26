# Generated by Django 3.0.3 on 2020-06-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0004_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventid', models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50)),
                ('description', models.TextField(default=None)),
                ('date_start', models.DateField(default=None)),
                ('place', models.TextField(default=None)),
                ('time', models.TimeField(default=None)),
                ('coverImage', models.ImageField(default=None, upload_to='')),
                ('detailTxt', models.TextField(default=None)),
                ('detailUrl', models.URLField(default=None)),
                ('ticketUrl', models.URLField(blank=True)),
            ],
        ),
    ]
