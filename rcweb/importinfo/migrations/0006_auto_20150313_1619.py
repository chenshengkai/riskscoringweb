# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('importinfo', '0005_auto_20150313_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='annual_income',
            field=models.DecimalField(default=0, verbose_name='\u5e74\u6536\u5165', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 19, 39, 220350, tzinfo=utc), verbose_name='\u5bfc\u5165\u65e5\u671f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bureauloandetail',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 19, 39, 222077, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bureauloanrepayment',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 19, 39, 222969, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bureaupfund',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 8, 19, 39, 223725, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
