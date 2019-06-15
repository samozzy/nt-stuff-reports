# Generated by Django 2.2 on 2019-06-15 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0017_auto_20190615_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayreport',
            name='approx_footfall',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dayreport',
            name='auditorium_bar_sales',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dayreport',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 15, 3, 25, 44, 429236), unique=True),
        ),
        migrations.AlterField(
            model_name='dayreport',
            name='studio_bar_sales',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 3, 25, 44, 431559)),
        ),
    ]
