# Generated by Django 2.2 on 2019-06-15 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0015_auto_20190615_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 3, 22, 48, 790138)),
        ),
    ]
