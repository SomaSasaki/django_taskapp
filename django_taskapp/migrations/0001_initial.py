# Generated by Django 3.2.8 on 2021-11-06 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.date(2021, 11, 6))),
                ('time', models.TimeField(default=datetime.time(12, 0))),
                ('detail', models.TextField(blank=True)),
                ('author', models.CharField(default='あなた', max_length=20)),
            ],
        ),
    ]
